"""
__author__ = "Piermuz"
__copyright__ = "Copyright 2023, Italian Tax ID Code Calculator"
__credits__ = ["Piermichele Rosati"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Piermichele Rosati"
__email__ = "piermichele.rosati@gmail.com"
"""

import os
import pandas as pd
import argparse


class Person:

    def __init__(self, surname, name, birth_year, birth_month, birth_day, birth_place, gender):
        self.surname = surname
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.birth_place = birth_place
        self.gender = gender

    def __str__(self):
        return f"Surname: {self.surname}\n" \
               f"Name: {self.name}\n" \
               f"Birthday: {self.birth_day}/{self.birth_month}/{self.birth_year}\n" \
               f"Gender: {self.gender}"


class ItalianTaxIDCalculator(object):
    __instance = None
    __number_month = {}

    @staticmethod
    def get_instance():
        if ItalianTaxIDCalculator.__instance is None:
            ItalianTaxIDCalculator()
        return ItalianTaxIDCalculator.__instance

    def __init__(self):
        if ItalianTaxIDCalculator.__instance is not None:
            raise Exception("This class is a singleton!")
        ItalianTaxIDCalculator.__instance = self
        self.__initialize_dict()

    def generate_tax_ID(self, person):
        s = (self.__calculate_surname_characters(person.surname) +
             self.__calculate_first_name_characters(person.name) +
             self.__calculate_birth_year_characters(person.birth_year) +
             self.__calculate_birth_month_characters(person.birth_month) +
             self.__calculate_birth_day_gender_characters(person.gender, person.birth_day) +
             self.__calculate_birth_place_characters(person.birth_place)).upper()
        return s + self.__calculate_control_character(s)

    def __calculate_surname_characters(self, surname):
        surname = self.__clean_string(surname)
        vowels = self.__get_vowels(surname)
        cons = self.__get_consonants(surname)
        surname_chars = cons[0]

        if len(cons) >= 3:
            surname_chars += cons[1]
            surname_chars += cons[2]
        if len(cons) == 2:
            surname_chars += cons[1]
            surname_chars += vowels[0]
        if len(cons) == 1 and len(vowels) == 1:
            surname_chars += vowels[0]
            surname_chars += 'x'
        elif len(cons) == 1:
            surname_chars += vowels[0]
            surname_chars += vowels[1]

        return surname_chars

    def __calculate_first_name_characters(self, name):
        name_chars = ""
        name = self.__clean_string(name)
        vowels = self.__get_vowels(name)
        cons = self.__get_consonants(name)
        name_chars += cons[0]
        if len(cons) >= 4:
            name_chars += cons[2]
            name_chars += cons[3]
        elif len(cons) >= 3:
            name_chars += cons[1]
            name_chars += cons[2]
        if len(cons) == 2:
            name_chars += cons[1]
            name_chars += vowels[0]
        if len(cons) == 1 and len(vowels) >= 2:
            name_chars += vowels[0]
            name_chars += vowels[1]
        elif len(cons) == 1 and len(vowels) == 1:
            name_chars += vowels[0]
            name_chars += "x"
        return name_chars

    def __calculate_birth_year_characters(self, year):
        s = str(year)
        return s[2] + s[3]

    def __calculate_birth_month_characters(self, month):
        return self.__number_month[month]

    def __calculate_birth_day_gender_characters(self, gender, birth_day):
        s = str(birth_day)
        if gender == "M":
            if len(s) == 1:
                s = "0" + s
        else:
            s = str(birth_day + 40)
        return s

    def __calculate_birth_place_characters(self, birth_place):
        path_cadastral_codes = os.path.abspath("./resources/cadastral_codes.csv")
        df = pd.read_csv(path_cadastral_codes, delimiter=',')
        return df.loc[df['DENOMINATION'] == birth_place.upper(), 'ENTE_CODE'].iloc[0]

    def __calculate_control_character(self, s):
        c = 0
        path_conversion = "./resources/convertion_character_by_position.csv"
        df = pd.read_csv(path_conversion, delimiter=',')
        for i in range(len(s)):
            if not i % 2 == 0:
                c += df.loc[df['CHAR'] == s[i].upper(), 'CHAR_CONVERSION_EVEN'].iloc[0]
            else:
                c += df.loc[df['CHAR'] == s[i].upper(), 'CHAR_CONVERSION_ODD'].iloc[0]
        return chr((c % 26) + 65)  # necessary sum 65, 'A' character

    def __initialize_dict(self):
        self.__number_month.update({1: 'a'})
        self.__number_month.update({2: 'b'})
        self.__number_month.update({3: 'c'})
        self.__number_month.update({4: 'd'})
        self.__number_month.update({5: 'e'})
        self.__number_month.update({6: 'h'})
        self.__number_month.update({7: 'l'})
        self.__number_month.update({8: 'm'})
        self.__number_month.update({9: 'p'})
        self.__number_month.update({10: 'r'})
        self.__number_month.update({11: 's'})
        self.__number_month.update({12: 't'})

    def __clean_string(self, s):
        s = s.replace("'", "")
        s = s.replace(" ", "")
        return s.lower()

    def __get_vowels(self, s):
        if not self.__contains_vowels(s):
            return None
        tmp = ""
        for c in s:
            if self.__is_vowel(c):
                tmp += c
        return tmp

    def __get_consonants(self, s):
        if not self.__contains_consonants(s):
            return None
        tmp = ""
        for c in s:
            if self.__is_consonant(c):
                tmp += c
        return tmp

    def __contains_vowels(self, s):
        return len(list(filter(lambda c: self.__is_vowel(c), s))) != 0

    def __is_vowel(self, c):
        return c in list("aeiou")

    def __contains_consonants(self, s):
        for c in s:
            if self.__is_consonant(c):
                return True
        return False

    def __is_consonant(self, c):
        return not self.__is_vowel(c)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="tax_id_calculator",
        description="Calculate the Italian Tax ID for the given person data",
        epilog="Piermuz thanks you for using %(prog)s ;)",
    )
    parser.add_argument('-s', '--surname', help="the surname", type=str, required=True)
    parser.add_argument('-n', '--name', help="the name", type=str, required=True)
    parser.add_argument('-y', '--year', help="the year of birth", type=int, required=True)
    parser.add_argument('-m', '--month', help="the month of birth", type=int, required=True)
    parser.add_argument('-d', '--day', help="the day of birth", type=int, required=True)
    parser.add_argument('-p', '--place', help="the place of birth. Remember to use \"\" if the place of birth "
                                              "contains spaces ", type=str, required=True)
    parser.add_argument('-g', '--gender', help="the gender", type=str, required=True)
    args = parser.parse_args()
    p0 = Person(args.surname, args.name, args.year, args.month, args.day, args.place, args.gender)
    print(p0)
    generator = ItalianTaxIDCalculator().get_instance()
    print(f"Tax ID code: {generator.generate_tax_ID(p0)}")
