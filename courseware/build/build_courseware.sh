#!/bin/bash
# Build every courseware artifact from the single source (course_data.py + data_domainN.py).
set -e
cd "$(dirname "$0")"
python3 build_slides.py
python3 build_lesson_plan.py
python3 build_learner_guide.py
echo "All courseware artifacts rebuilt."
