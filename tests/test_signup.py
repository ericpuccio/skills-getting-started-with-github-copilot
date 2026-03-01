from urllib.parse import quote


def test_signup_success_aaa(client):
    # Arrange
    activity = "Tennis Club"
    email = "tester@example.com"
    url = f"/activities/{quote(activity, safe='')}/signup"

    # Act
    resp = client.post(url, params={"email": email})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")

    # Verify participant added
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate_aaa(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    url = f"/activities/{quote(activity, safe='')}/signup"

    # Act
    resp = client.post(url, params={"email": existing})

    # Assert
    assert resp.status_code == 400


def test_signup_activity_not_found_aaa(client):
    # Arrange
    activity = "No Such Activity"
    email = "noone@nowhere.edu"
    url = f"/activities/{quote(activity, safe='')}/signup"

    # Act
    resp = client.post(url, params={"email": email})

    # Assert
    assert resp.status_code == 404
