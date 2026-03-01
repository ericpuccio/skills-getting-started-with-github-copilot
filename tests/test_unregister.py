from urllib.parse import quote


def test_unregister_success_aaa(client):
    # Arrange
    activity = "Gym Class"
    email = "john@mergington.edu"
    url = f"/activities/{quote(activity, safe='')}/participants"

    # Precondition check (arrange)
    before = client.get("/activities").json()
    assert email in before[activity]["participants"]

    # Act
    resp = client.delete(url, params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Removed" in resp.json().get("message", "")

    after = client.get("/activities").json()
    assert email not in after[activity]["participants"]


def test_unregister_student_not_found_aaa(client):
    # Arrange
    activity = "Gym Class"
    missing = "noone@nowhere.edu"
    url = f"/activities/{quote(activity, safe='')}/participants"

    # Act
    resp = client.delete(url, params={"email": missing})

    # Assert
    assert resp.status_code == 404


def test_unregister_activity_not_found_aaa(client):
    # Arrange
    activity = "No Such Activity"
    email = "someone@nowhere.edu"
    url = f"/activities/{quote(activity, safe='')}/participants"

    # Act
    resp = client.delete(url, params={"email": email})

    # Assert
    assert resp.status_code == 404
