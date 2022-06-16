# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from romkan import (
    expand_consonant,
    to_hepburn,
    to_hiragana,
    to_kana,
    to_katakana,
    to_kunrei,
    to_roma,
    is_consonant,
    is_vowel,
)


def test_to_katakana():
    assert to_katakana("kanji") == "カンジ"
    assert to_katakana("kanzi") == "カンジ"
    assert to_katakana("kannji") == "カンジ"
    assert to_katakana("chie") == "チエ"
    assert to_katakana("tie") == "チエ"
    assert to_katakana("kyouju") == "キョウジュ"
    assert to_katakana("syuukyou") == "シュウキョウ"
    assert to_katakana("shuukyou") == "シュウキョウ"
    assert to_katakana("saichuu") == "サイチュウ"
    assert to_katakana("saityuu") == "サイチュウ"
    assert to_katakana("cheri-") == "チェリー"
    assert to_katakana("tyeri-") == "チェリー"
    assert to_katakana("shinrai") == "シンライ"
    assert to_katakana("sinrai") == "シンライ"
    assert to_katakana("hannnou") == "ハンノウ"
    assert to_katakana("han'nou") == "ハンノウ"

    assert to_katakana("wo") == "ヲ"
    assert to_katakana("we") == "ウェ"
    assert to_katakana("du") == "ヅ"
    assert to_katakana("she") == "シェ"
    assert to_katakana("di") == "ヂ"
    assert to_katakana("fu") == "フ"
    assert to_katakana("ti") == "チ"
    assert to_katakana("wi") == "ウィ"

    assert to_katakana("je") == "ジェ"
    assert to_katakana("e-jento") == "エージェント"


def test_to_hiragana():
    assert to_hiragana("kanji") == "かんじ"
    assert to_hiragana("kanzi") == "かんじ"
    assert to_hiragana("kannji") == "かんじ"
    assert to_hiragana("chie") == "ちえ"
    assert to_hiragana("tie") == "ちえ"
    assert to_hiragana("kyouju") == "きょうじゅ"
    assert to_hiragana("syuukyou") == "しゅうきょう"
    assert to_hiragana("shuukyou") == "しゅうきょう"
    assert to_hiragana("saichuu") == "さいちゅう"
    assert to_hiragana("saityuu") == "さいちゅう"
    assert to_hiragana("cheri-") == "ちぇりー"
    assert to_hiragana("tyeri-") == "ちぇりー"
    assert to_hiragana("shinrai") == "しんらい"
    assert to_hiragana("sinrai") == "しんらい"
    assert to_hiragana("hannnou") == "はんのう"
    assert to_hiragana("han'nou") == "はんのう"


def test_to_kana():
    assert to_kana("kanji") == "カンジ"
    assert to_kana("kanzi") == "カンジ"
    assert to_kana("kannji") == "カンジ"
    assert to_kana("chie") == "チエ"
    assert to_kana("tie") == "チエ"
    assert to_kana("kyouju") == "キョウジュ"
    assert to_kana("syuukyou") == "シュウキョウ"
    assert to_kana("shuukyou") == "シュウキョウ"
    assert to_kana("saichuu") == "サイチュウ"
    assert to_kana("saityuu") == "サイチュウ"
    assert to_kana("cheri-") == "チェリー"
    assert to_kana("tyeri-") == "チェリー"
    assert to_kana("shinrai") == "シンライ"
    assert to_kana("sinrai") == "シンライ"
    assert to_kana("hannnou") == "ハンノウ"
    assert to_kana("han'nou") == "ハンノウ"

    assert to_kana("wo") == "ヲ"
    assert to_kana("we") == "ウェ"
    assert to_kana("du") == "ヅ"
    assert to_kana("she") == "シェ"
    assert to_kana("di") == "ヂ"
    assert to_kana("fu") == "フ"
    assert to_kana("ti") == "チ"
    assert to_kana("wi") == "ウィ"

    assert to_kana("je") == "ジェ"
    assert to_kana("e-jento") == "エージェント"


def test_to_hepburn():
    assert to_hepburn("kannzi") == "kanji"
    assert to_hepburn("tie") == "chie"

    assert to_hepburn("KANNZI") == "kanji"
    assert to_hepburn("TIE") == "chie"

    assert to_hepburn("カンジ") == "kanji"
    assert to_hepburn("チエ") == "chie"

    assert to_hepburn("かんじ") == "kanji"
    assert to_hepburn("ちえ") == "chie"

    assert to_hepburn("しゃしん") == "shashin"
    assert to_hepburn("しゅっしょう") == "shusshou"


def test_to_kunrei():
    assert to_kunrei("kanji") == "kanzi"
    assert to_kunrei("chie") == "tie"

    assert to_kunrei("KANJI") == "kanzi"
    assert to_kunrei("CHIE") == "tie"

    assert to_kunrei("カンジ") == "kanzi"
    assert to_kunrei("チエ") == "tie"

    assert to_kunrei("かんじ") == "kanzi"
    assert to_kunrei("ちえ") == "tie"

    assert to_kunrei("しゃしん") == "syasin"
    assert to_kunrei("しゅっしょう") == "syussyou"


def test_to_roma():
    assert to_roma("カンジ") == "kanji"
    assert to_roma("チャウ") == "chau"
    assert to_roma("ハンノウ") == "han'nou"

    assert to_roma("かんじ") == "kanji"
    assert to_roma("ちゃう") == "chau"
    assert to_roma("はんのう") == "han'nou"


def test_is_consonant():
    assert not is_consonant("a")
    assert is_consonant("k")


def test_is_vowel():
    assert is_vowel("a")
    assert not is_vowel("z")


def test_expand_consonant():
    assert sorted(expand_consonant("k")) == ["ka", "ke", "ki", "ko", "ku"]
    assert sorted(expand_consonant("s")) == ["sa", "se", "si", "so", "su"]
    assert sorted(expand_consonant("t")) == ["ta", "te", "ti", "to", "tu"]

    assert sorted(expand_consonant("ky")) == ["kya", "kyo", "kyu"]
    assert sorted(expand_consonant("kk")) == ["kka", "kke", "kki", "kko", "kku"]
    assert sorted(expand_consonant("sh")) == ["sha", "she", "shi", "sho", "shu"]
    assert sorted(expand_consonant("sy")) == ["sya", "sye", "syo", "syu"]
    assert sorted(expand_consonant("ch")) == ["cha", "che", "chi", "cho", "chu"]
