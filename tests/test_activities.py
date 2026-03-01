def test_get_activities_aaa(client):
    # Arrange

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Ensure known activities exist in the initial fixture data
    assert "Chess Club" in data
    assert "Programming Class" in data
