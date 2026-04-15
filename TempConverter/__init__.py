import check50
import check50.java
import re


@check50.check()
def exists():
    """PA03.java exists"""
    check50.exists("PA03.java")


@check50.check(exists)
def compiles():
    """PA03.java compiles"""
    check50.java.compile("PA03.java")


@check50.check(compiles)
def checkHeader():
    """file has a header comment at the top"""
    with open("PA03.java") as f:
        contents = f.read()
    # Expects a block comment (/* ... */) or line comment (//) near the top
    if not re.search(r"^\s*(//|/\*)", contents, re.MULTILINE):
        raise check50.Failure("No header comment found at the top of PA03.java")


@check50.check(compiles)
def test1():
    """converts 70°F to Celsius"""
    check50.java.run("PA03").stdin("70").stdout(
        r".*[Ff]ahrenheit.*\n.*21\.1+.*", regex=True
    )


@check50.check(compiles)
def test2():
    """converts 32°F to Celsius"""
    check50.java.run("PA03").stdin("32").stdout(
        r".*[Ff]ahrenheit.*\n.*0\.0.*", regex=True
    )


@check50.check(compiles)
def test3():
    """converts 0°F to Celsius"""
    check50.java.run("PA03").stdin("0").stdout(
        r".*[Ff]ahrenheit.*\n.*-17\.7+.*", regex=True
    )


@check50.check(compiles)
def test4():
    """converts 102°F to Celsius"""
    check50.java.run("PA03").stdin("102").stdout(
        r".*[Ff]ahrenheit.*\n.*38\.8+.*", regex=True
    )


@check50.check(compiles)
def test5():
    """converts -32°F to Celsius"""
    check50.java.run("PA03").stdin("-32").stdout(
        r".*[Ff]ahrenheit.*\n.*-35\.5+.*", regex=True
    )


@check50.check(compiles)
def hiddenTest():
    """converts a hidden temperature to Celsius"""
    # Example hidden input: 212°F -> 100.0°C
    check50.java.run("PA03").stdin("212").stdout(
        r".*[Ff]ahrenheit.*\n.*100\.0.*", regex=True
    )
