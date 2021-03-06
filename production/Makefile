#!/usr/bin/env bash
root_project = ..
build = "$(root_project)/www"
release = "$(root_project)/production/release"

BG =\n\033[0;36m-- # Beginning
NC =\033[0m\n# No Color

version := $(shell git describe --tags --match="v*")

.PHONY: all
all: clean app

.PHONY: clean
clean:
	@(printf "${BG}Cleaning project${NC}")
		rm -rf $(build)
		rm -rf $(target)

.PHONY: npm
npm:
	@(printf "${BG}Installing NPM dependencies${NC}")
		cd $(root_project) && npm install

.PHONY: pip
pip:
	@(printf "${BG}Installing pip dependencies${NC}")
		pip3 install -r $(root_project)/requirements.txt

.PHONY: app
app: pip npm tests
	@(printf "${BG}Preparing build directory${NC}")
		mkdir -p $(build)
		mkdir -p $(release)

	@(printf "${BG}Generating version file${NC}")
		echo "VERSION=$(version)" >$(build)/version.txt
		echo "BUILD_DATE=$(shell date --utc +%FT%TZ)" >>$(build)/version.txt

	@(printf "${BG}Generating pages${NC}")
		cd $(root_project) && python3 generate.py "$(version)"

	@(printf "${BG}Running Gulp tasks${NC}")
		cd $(root_project) && export FORCE_COLOR=1 && node_modules/.bin/gulp production --appVersion=$(version)

.PHONY: package
package: app
	@(printf "${BG}Creating ZIP package version $(version)${NC}")
		cd $(build) && zip -r $(release)/telco-obeznik.zip * .[^.]*
		echo $(version) > $(release)/latest.version

.PHONY: tests
tests:
	@(printf "${BG}Running Unit Tests${NC}")
		cd $(root_project) && python3 -m unittest tests/**/*.py
