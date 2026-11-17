"""Small regression suite for numbering, page scopes, and answer pairing."""
import unittest
import pymupdf as fitz
import index


class IndexTests(unittest.TestCase):
    def document(self,text):
        d=fitz.open();p=d.new_page();p.insert_text((50,60),text,fontsize=12)
        return d

    def record(self,contest,role='questions',part='day2'):
        return dict(id='test',contest=contest,role=role,part=part,year=2020,title='test')

    def test_imc_day_two_starts_at_five(self):
        d=self.document('Problem 5. first\nProblem 6. second\nProblem 7. third\nProblem 8. fourth')
        self.assertEqual([a['number'] for a in index.anchors(d,self.record('IMC'))],['5','6','7','8'])

    def test_standalone_cmo_heading(self):
        d=self.document('1.\nStatement\n2.\nAnother statement')
        self.assertEqual([a['number'] for a in index.anchors(d,self.record('CMO'))],['1','2'])

    def test_yau_question_heading(self):
        d=self.document('Question 1. first\nQuestion 2. second')
        self.assertEqual(len(index.anchors(d,self.record('YAU'))),2)

    def test_putnam_numbering(self):
        d=self.document('A1 first\nA2 second\nA3 third\nA4 fourth\nA5 fifth\nA6 sixth\nB1 seventh')
        self.assertEqual(index.anchors(d,self.record('PUTNAM'))[-1]['number'],'B1')

    def test_egmo_language_pairing(self):
        self.assertEqual(index.pair_key(self.record('EGMO',part='day1-English')),index.pair_key(self.record('EGMO','solutions','both-days')))

    def test_year_and_round_do_not_cross_pair(self):
        a=self.record('CHSMO',part='A-round1');b=self.record('CHSMO',part='A-additional')
        self.assertNotEqual(index.pair_key(a),index.pair_key(b))
        b={**a,'year':2021};self.assertNotEqual(index.pair_key(a),index.pair_key(b))

    def test_cmc_main_sections_not_fill_in_sequence(self):
        d=self.document('placeholder')
        index.OCR['test']={'pages':[[('一、填空题',[40,100,200,120]),('1. first',[40,130,200,145]),('2. second',[40,160,200,175]),('二、计算题',[40,200,200,220])]]}
        anchors=index.anchors(d,self.record('CMC'))
        self.assertEqual([a['number'] for a in anchors],['1','2'])
        self.assertTrue(all(a['grouped'] for a in anchors))
        index.OCR.pop('test')


if __name__=='__main__':unittest.main()
