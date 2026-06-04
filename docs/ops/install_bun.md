# Procedure: Install Bun

## Objective
Install the Bun runtime required for Archon.

## Procedure
1. Execute installation: `curl -fsSL https://bun.sh/install | bash`
2. Add to PATH (if not automatic): `export BUN_INSTALL="/home/exocrat/.bun" && export PATH="/bin:/home/exocrat/.npm/_npx/d07ada7b4a99c96e/node_modules/.bin:/home/exocrat/node_modules/.bin:/home/node_modules/.bin:/node_modules/.bin:/usr/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Users/thalp/AppData/Local/Microsoft/WindowsApps:/snap/bin"`

## Verification
- Confirm installation: `~/.bun/bin/bun --version`
