-- Drop the table if it exists
DROP TABLE IF EXISTS users;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    UserID SERIAL PRIMARY KEY,
    Username VARCHAR(50) UNIQUE,
    Email VARCHAR(100) UNIQUE,
    PasswordHash VARCHAR(255),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    RoleID INTEGER,
    DepartmentID INTEGER,
    IsActive INTEGER,
    LastLogin TIMESTAMP,
    CreatedAt TIMESTAMP,
    UpdatedAt TIMESTAMP,
    ProfilePictureURL VARCHAR(255),
    Phone VARCHAR(20),
    Timezone VARCHAR(50),
    Language VARCHAR(50)
);
