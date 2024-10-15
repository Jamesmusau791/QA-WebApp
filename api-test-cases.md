# API Test Cases

| Test Case ID | Endpoint              | Method | Description                    | Expected Result |
|--------------|-----------------------|--------|--------------------------------|-----------------|
| API-001      | `/users`              | GET    | Fetch all users                | 200 OK with user data |
| API-002      | `/albums/1`           | GET    | Fetch album with ID = 1        | 200 OK with album data |
| API-003      | `/albums`             | POST   | Create a new album             | 201 Created |
| API-004      | `/photos?albumId=1`   | GET    | Fetch photos for album ID = 1  | 200 OK with photo data |

