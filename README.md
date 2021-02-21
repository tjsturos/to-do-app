# Todo App
This Todo application is built for tasks and then syncing them to the cloud.

The application is built to showcase, as well as learn, Hybrid mobile apps and general application development.

## Tech Stack
### Application Data Storage Solution
The application will store data in a PostgresSQL database.
### Application Server/API
The application will have data handled by a REST API that will be built with Python, utilizing the Apache2 framework.

### Supported Application Clients
The application's initial client will be built using a hybrid application toolchain.

#### Hybrid tool
The tool is not yet chosen.

The hybrid application will deploy apps to Android and iOS platforms.

There may be additional clients, such as PWA/Web app or Desktop, in the future.

### Application Hosting Environment
The application will be hosted in Google Cloud Platform (GCP).

## Continuous Integration
The application will be deployable to the production initially just by merging feature branches into the master branch.  In the future, the branches, when pushed to, will build review/temporary environments.

Automated tests will be integrated into this solution, as to run the tests in the cloud environment to ensure that everything runs in production before it gets deployed.

## Automated Testing
Automated tests should able to be run both in the local environments, as well as the cloud.  There should be some feature tests, as well as e2e (end to end) tests.