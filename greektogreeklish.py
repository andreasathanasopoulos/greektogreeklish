# -*- coding: utf-8 -*-
import os, argparse, shutil
from os import walk

class GreekToGreeklish(object):

    ACCENT_MAPPING = {
        u'Ά': u'Α', u'ά': u'α', u'Έ': u'Ε', u'έ': u'ε',
        u'Ή': u'η', u'ή': u'η', u'Ί': u'Ι', u'ί': u'ι',
        u'Ό': u'Ο', u'ό': u'ο', u'Ύ': u'Υ', u'ύ': u'υ',
        u'Ώ': u'Ω', u'ώ': u'ω',
    }
    GR_TO_ENG = {
        u'Α': u'A', u'α': u'a', u'Β': u'V', u'β': u'v',
        u'Γ': u'G', u'γ': u'g', u'Δ': u'D', u'δ': u'd',
        u'Ε': u'E', u'ε': u'e', u'Ζ': u'Z', u'ζ': u'z',
        u'Η': u'I', u'η': u'i', u'Θ': u'TH', u'θ': u'th',
        u'Ι': u'I', u'ι': u'i', u'Κ': u'K', u'κ': u'k',
        u'Λ': u'L', u'λ': u'l', u'Μ': u'M', u'μ': u'm',
        u'Ν': u'N', u'ν': u'n', u'Ξ': u'KS', u'ξ': u'ks',
        u'Ο': u'O', u'ο': u'o', u'Π': u'P', u'π': u'p',
        u'Ρ': u'R', u'ρ': u'r', u'Σ': u'S', u'σ': u's',
        u'Τ': u'T', u'τ': u't', u'Υ': u'I', u'υ': u'i',
        u'Φ': u'F', u'φ': u'f', u'Χ': u'CH', u'χ': u'ch',
        u'Ψ': u'PS', u'ψ': u'ps', u'Ω': u'O', u'ω': u'o',
        u'ς': u's', u' ': u'_',
        u'ΑΙ': u'ai', u'Αι': u'Ai', u'αΙ': u'aI', u'αι': u'ai',
        u'ΕΥ': u'EF', u'Ευ': u'Ef', u'εΥ': u'eF', u'ευ': u'ef',
        u'ΑΥ': u'AF', u'Αυ': u'Af', u'αΥ': u'aF', u'αυ': u'af',
        u'ΟΥ': u'OU', u'Ου': u'Ou', u'οΥ': u'oU', u'ου': u'ou',
        u'ΕΙ': u'I', u'Ει': u'I', u'εΙ': u'i', u'ει': u'i',
        u'ΟΙ': u'I', u'Οι': u'I', u'οΙ': u'i', u'οι': u'i',
        u'ΜΠ': u'MP', u'Μπ': u'Mp', u'μΠ': u'mP', u'μπ': u'mp',
        u'ΝΤ': u'NT', u'Ντ': u'Nt', u'νΤ': u'nT', u'ντ': u'nt',
        u'ΓΚ': u'G', u'Γκ': u'G', u'γΚ': u'g', u'γκ': u'g',
        u'ΓΓ': u'G', u'Γγ': u'G', u'γΓ': u'g', u'γγ': u'g',
        # u'': u'', u'': u'', u'': u'', u'': u'',
    }

    def __init__(self):
        parser = argparse.ArgumentParser(
            description = "Description for my parser"
            )
        parser.add_argument(
            "-I",
            "--Input",
            help = "When we need to add specific input location",
            required = False,
            default = os.getcwd()
        )
        parser.add_argument(
            "-O",
            "--Output",
            help = "When we need to add specific output location",
            required = False,
            default = os.getcwd()
        )
        argument = parser.parse_args()
        self.input = argument.Input
        self.output = argument.Output
        self.f = [] # empty list of filenames
        for (dirpath, dirnames, filenames) in walk(self.input):
            self.f.extend(filenames)
            break
    def printfilenames(self):
        print(self.f)

    def transform(self):
        for file in self.f:
            file = list(file)
            newfile = list(file)
            for i, letter in enumerate(newfile):
                if letter in self.ACCENT_MAPPING:
                    letter = self.ACCENT_MAPPING[letter]
                if letter in self.GR_TO_ENG:
                    newfile[i] = self.GR_TO_ENG[letter]
            src_file = os.path.join(self.input, ''.join(file))
            dest_file = os.path.join(self.output, ''.join(newfile))
            if self.input != self.output:
                shutil.copy(src_file, self.output)
                src_file = os.path.join(self.output, ''.join(file))
            os.rename(
                src_file,
                dest_file
            )
            print(''.join(newfile))


if __name__ == '__main__':
    app = GreekToGreeklish()
    app.transform()
