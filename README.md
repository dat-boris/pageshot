pageshot
#############################

Take screenshot of specific URL.

[![Circle CI](https://circleci.com/gh/mobify/pageshot.svg?style=svg&circle-token=<cirlce-ci-token>)](https://circleci.com/gh/mobify/pageshot)

[![Coverage Status](https://coveralls.io/repos/mobify/pageshot/badge.svg?branch=master&service=github)](https://coveralls.io/github/mobify/pageshot?branch=master)


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
