#!/bin/bash

python3 -m render_unittest render
if [ $? -eq 0 ]; then
    echo "Tests unitaires OK"
else
    echo "Tests unitaires échoués"
fi

python3 -m render_integration_test render
if [ $? -eq 0 ]; then
    echo "Tests d'intégration OK"
else
    echo "Tests d'intégration échoués"
fi