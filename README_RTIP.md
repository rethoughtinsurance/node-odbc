## RTIP ODBC

This is a fork of the repository `git://github.com/wankdanker/node-odbc.git`

It contains changes to use prebuild binaries so that the module doesn't
rebuild anytime another package is added or removed.

Currently, we only have prebuilds for Mac OS X.

### Creating the prebuild binaries

Use `prebuild` to build the prebuilds. In the root directory run:
```code
> prebuild -t 10.0.0 -r node
```
Then, upload to git:
```code
> prebuild -t 10.0.0 -r node -u <github token>
```

### Upload to Nexus

From the command prompt use `npm login`:
```code
> npm login --registry=http://54.156.254.122:8081/repository/rtip-npm-private/
```

Then, to publish to the Nexus repository:
```code
> npm publish --registry=http://54.156.254.122:8081/repository/rtip-npm/
```

### Installing the rtip-odbc module
Login to npm (yarn):
```code
> npm login --registry=http://54.156.254.122:8081/repository/rtip-npm/
```

Install the module:
```code
npm --registry=http://54.156.254.122:8081/repository/rtip-npm/ install rtip-odbc
```
