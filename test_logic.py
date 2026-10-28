from resume_checker import analyze_resume

def test_logic():
    print("--- Test 1: Full Match ---")
    res1 = analyze_resume(
        resume_text="Experienced in Python, SQL, Docker, and AWS.",
        job_desc="We need skills in Python, SQL, Docker, and AWS."
    )
    print(f"Resume Score: {res1['resume_score']}%, Match: {res1['match_score']}%")
    print(f"Matched Skills: {res1['skills']}")
    print(f"Missing: {res1['missing']}")
    assert res1['match_score'] == 100
    assert len(res1['missing']) == 0

    print("\n--- Test 2: Partial Match & Missing Skills ---")
    res2 = analyze_resume(
        resume_text="Junior developer skilled in Python, JavaScript, and HTML.",
        job_desc="Required: Python, React, TypeScript, Docker, and Kubernetes."
    )
    print(f"Resume Score: {res2['resume_score']}%, Match: {res2['match_score']}%")
    print(f"Matched Skills: {res2['skills']}")
    print(f"Missing: {res2['missing']}")
    print(f"Radar labels: {res2['radar_labels']}")
    assert "python" in res2['skills']
    assert "react" in res2['missing']
    assert "typescript" in res2['missing']

    print("\n--- Test 3: Substring Collisions (java vs javascript) ---")
    res3 = analyze_resume(
        resume_text="Proficient in JavaScript and Django.",
        job_desc="Looking for Java, Go, and C++."
    )
    # Javascript should NOT match Java! Django should NOT match Go!
    print(f"Matched Skills: {res3['skills']}")
    print(f"All resume skills: {res3['all_resume_skills']}")
    assert "java" not in res3['all_resume_skills']
    assert "go" not in res3['all_resume_skills']
    assert "javascript" in res3['all_resume_skills']
    print("[PASS] Substring collision checks passed!")

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    test_logic()
