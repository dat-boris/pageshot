pageshot
--------

Take screenshot of specific URL.

[![Circle CI](https://circleci.com/gh/dat-boris/pageshot.svg?style=svg)](https://circleci.com/gh/dat-boris/pageshot)

# Examples

    import pageshot

    s = pageshot.Screenshoter()
    s.take_screenshot("http://www.google.com", "out.png")

# Installing

We require phantomjs support.

    npm -g install phantomjs

To install, include this in requirements.txt

    git+https://github.com/sketchytechky/pageshot.git


# Running Tests

Run test with

    py.test --pep8

To run test in watch mode

	py.test.watch -- --pep8
	# same with: ptw -- --pep8
