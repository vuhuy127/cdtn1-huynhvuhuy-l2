# Required real screenshots for BT3

Do not create illustrative or edited images and label them as runtime evidence. Capture these screenshots from the student's own Docker-capable machine after following the Deployment Guide:

1. `pytest-pass.png` — terminal showing `python -m pytest -q` and all 12 tests passing.
2. `compose-healthy.png` — terminal showing `docker compose ps` with the `app` service as `healthy`.
3. `clean-machine-v1.0.png` — terminal showing clone of the public `v1.0` tag into a new empty folder, successful `docker compose up -d --build`, and successful `/health` response.

Hide private paths or personal data. The build environment used for the current source test does not have a Docker executable, so screenshots 2 and 3 must be captured by the student on a Docker-capable machine.
