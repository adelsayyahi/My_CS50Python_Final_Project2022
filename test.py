# test_project.py
import project


def test_determine_fatty_liver_prob():
    assert project.determine_fatty_liver_prob(20) == "Low probability"
    assert project.determine_fatty_liver_prob(27) == "Moderate probability"
    assert project.determine_fatty_liver_prob(32) == "High probability"


def test_determine_fatty_liver_degree():
    assert project.determine_fatty_liver_degree(20) == "Normal"
    assert project.determine_fatty_liver_degree(27) == "Grade 1"
    assert project.determine_fatty_liver_degree(32) == "Grade 2 or higher"
