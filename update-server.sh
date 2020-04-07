#!/bin/bash

ssh -t brian@dangerouslemonade.com "cd dangerouslemonade && git pull && sudo systemctl restart dangerouslemonade.service"
