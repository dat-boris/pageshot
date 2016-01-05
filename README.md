pageshot
#############################

	 ___                     _        _    ____ _____ 
	|_ _|_ __  ___  ___ _ __| |_     / \  |  _ \_   _|
	 | || '_ \/ __|/ _ \ '__| __|   / _ \ | |_) || |  
	 | || | | \__ \  __/ |  | |_   / ___ \|  _ < | |  
	|___|_| |_|___/\___|_|   \__| /_/   \_\_| \_\|_|  


[![Circle CI](https://circleci.com/gh/mobify/pageshot.svg?style=svg&circle-token=<cirlce-ci-token>)](https://circleci.com/gh/mobify/pageshot)

[![Coverage Status](https://coveralls.io/repos/mobify/pageshot/badge.svg?branch=master&service=github)](https://coveralls.io/github/mobify/pageshot?branch=master)

# Installing

To install this package, runs:

    pip install https://<deploy-access-token>@github.com/mobify/pageshot.git@<tagname>

Insert relevant version at `@<tagname>` (e.g. `@1.0.0`).

Remember to add the following line to `requirements.txt`

    git+https://<deploy-access-token>@github.com/mobify/pageshot.git@<tagname>

# Examples

	TODO: Insert examples here


# Running Tests

Run test with

    py.test --pep8

To run test in watch mode

	py.test.watch -- --pep8
	# same with: ptw -- --pep8
