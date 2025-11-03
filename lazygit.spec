%bcond_with devel
%global debug_package %{nil}

Name:           lazygit
Summary:        A simple terminal UI for git commands
Version:        0.56.0
Release:        1

%global tag     v%{version}
%global goipath github.com/jesseduffield/lazygit

# lazygit (MIT) bundles a number of go packages (Apache-2.0, BSD-2-Clause, BSD-3-Clause, MIT, Unlicense)
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND Unlicense

URL:            https://github.com/jesseduffield/lazygit
# use official release tarball (contains vendored dependencies)
Source0:        https://github.com/jesseduffield/%{name}/archive/%{tag}/%{name}-%{version}.tar.gz
Source1:        LICENSE.dependencies

BuildRequires:  golang

Provides:       bundled(golang(github.com/adrg/xdg) = v0.4.0
Provides:       bundled(golang(github.com/atotto/clipboard)) = 0.1.4
Provides:       bundled(golang(github.com/aybabtme/humanlog)) = 0.4.1
Provides:       bundled(golang(github.com/cloudfoundry/jibber_jabber)) = 0.0.0-20151120183258.bcc4c8345a21
Provides:       bundled(golang(github.com/creack/pty)) = 1.1.11
Provides:       bundled(golang(github.com/gdamore/tcell/v2)) = 2.8.1
Provides:       bundled(golang(github.com/go-errors/errors)) = 1.5.1
Provides:       bundled(golang(github.com/gookit/color)) = 1.4.2
Provides:       bundled(golang(github.com/imdario/mergo)) = 0.3.11
Provides:       bundled(golang(github.com/integrii/flaggy)) = 1.4.0
Provides:       bundled(golang(github.com/jesseduffield/generics)) = 0.0.0-20220320043834.727e535cbe68
Provides:       bundled(golang(github.com/jesseduffield/go-git/v5)) = 5.1.2-0.20221018185014.fdd53fef665d
Provides:       bundled(golang(github.com/jesseduffield/gocui)) = 0.3.1-0.20250220081214.b376cb0857ac
Provides:       bundled(golang(github.com/jesseduffield/kill)) = 0.0.0-20250101124109.e216ddbe133a
Provides:       bundled(golang(github.com/jesseduffield/lazycore)) = 0.0.0-20221012050358.03d2e40243c5
Provides:       bundled(golang(github.com/jesseduffield/minimal/gitignore)) = 0.3.3-0.20211018110810.9cde264e6b1e
Provides:       bundled(golang(github.com/kardianos/osext)) = 0.0.0-20190222173326.2bc1f35cddc0
Provides:       bundled(golang(github.com/karimkhaleel/jsonschema)) = 0.0.0-20231001195015.d933f0d94ea3
Provides:       bundled(golang(github.com/kyokomi/emoji/v2)) = 2.2.8
Provides:       bundled(golang(github.com/lucasb-eyer/go-colorful)) = 1.2.0
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = 0.0.16
Provides:       bundled(golang(github.com/mgutz/str)) = 1.2.0
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = 1.0.0
Provides:       bundled(golang(github.com/sahilm/fuzzy)) = 0.1.0
Provides:       bundled(golang(github.com/samber/lo)) = 1.31.0
Provides:       bundled(golang(github.com/sanity-io/litter)) = 1.5.2
Provides:       bundled(golang(github.com/sasha-s/go-deadlock)) = 0.3.5
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.4.2
Provides:       bundled(golang(github.com/spf13/afero)) = 1.9.5
Provides:       bundled(golang(github.com/spkg/bom)) = 0.0.0-20160624110644.59b7046e48ad
Provides:       bundled(golang(github.com/stefanhaller/git-todo-parser)) = 0.0.7-0.20240406123903.fd957137b6e2
Provides:       bundled(golang(github.com/stretchr/testify)) = 1.8.1
Provides:       bundled(golang(github.com/xo/terminfo)) = 0.0.0-20210125001918.ca9a967f8778
Provides:       bundled(golang(golang.org/x/exp)) = 0.0.0-20220318154914.8dddf5d87bd8
Provides:       bundled(golang(golang.org/x/sync)) = 0.11.0
Provides:       bundled(golang(gopkg.in/ozeidan/fuzzy-patricia.v3)) = 3.0.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1

# Indirect dependencies
Provides:       bundled(golang(github.com/bahlo/generic-list-go)) = 0.2.0
Provides:       bundled(golang(github.com/buger/jsonparser)) = 1.1.1
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides:       bundled(golang(github.com/emirpasic/gods)) = 1.12.0
Provides:       bundled(golang(github.com/fatih/color)) = 1.9.0
Provides:       bundled(golang(github.com/gdamore/encoding)) = 1.0.1
Provides:       bundled(golang(github.com/go-git/gcfg)) = 1.5.0
Provides:       bundled(golang(github.com/go-git/go-billy/v5)) = 5.0.0
Provides:       bundled(golang(github.com/go-logfmt/logfmt)) = 0.5.0
Provides:       bundled(golang(github.com/gobwas/glob)) = 0.2.3
Provides:       bundled(golang(github.com/invopop/jsonschema)) = 0.10.0
Provides:       bundled(golang(github.com/jbenet/go-context)) = 0.0.0-20150711004518.d14ea06fba99
Provides:       bundled(golang(github.com/kevinburke/ssh_config)) = 0.0.0-20190725054713.01f96b0aa0cd
Provides:       bundled(golang(github.com/konsorten/go-windows-terminal-sequences)) = 1.0.2
Provides:       bundled(golang(github.com/kr/logfmt)) = 0.0.0-20140226030751.b84e30acd515
Provides:       bundled(golang(github.com/kylelemons/godebug)) = 1.1.0
Provides:       bundled(golang(github.com/mailru/easyjson)) = 0.7.7
Provides:       bundled(golang(github.com/mattn/go-colorable)) = 0.1.11
Provides:       bundled(golang(github.com/mattn/go-isatty)) = 0.0.14
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = 1.1.0
Provides:       bundled(golang(github.com/onsi/ginkgo)) = 1.10.3
Provides:       bundled(golang(github.com/onsi/gomega)) = 1.7.1
Provides:       bundled(golang(github.com/petermattis/goid)) = 0.0.0-20240813172612.4fcff4a6cae7
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = 1.0.0
Provides:       bundled(golang(github.com/rivo/uniseg)) = 0.4.7
Provides:       bundled(golang(github.com/sergi/go-diff)) = 1.1.0
Provides:       bundled(golang(github.com/wk8/go-ordered-map/v2)) = 2.1.8
Provides:       bundled(golang(github.com/xanzy/ssh-agent)) = 0.2.1
Provides:       bundled(golang(golang.org/x/crypto)) = 0.31.0
Provides:       bundled(golang(golang.org/x/net)) = 0.33.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.30.0
Provides:       bundled(golang(golang.org/x/term)) = 0.29.0
Provides:       bundled(golang(golang.org/x/text)) = 0.22.0
Provides:       bundled(golang(gopkg.in/warnings.v0)) = 0.1.2

%description
lazygit provides an intuitive terminal interface for git operations,
making git's power more accessible without the complexity of the
command line.

%define gobuild go build -buildmode pie -compiler gc

%prep
%autosetup -n %{name}-%{version} -p1
cp %{SOURCE1} .

%build
%gobuild

%install
mkdir -p %{buildroot}/%{_bindir}
cp -pav lazygit %{buildroot}/%{_bindir}/

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%{_bindir}/lazygit
