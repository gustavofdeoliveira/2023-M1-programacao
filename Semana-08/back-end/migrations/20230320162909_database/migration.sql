-- CreateTable
CREATE TABLE "Coordinate" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "coordinateX" REAL NOT NULL,
    "coordinateY" REAL NOT NULL,
    "coordinateZ" REAL NOT NULL,
    "coordinateR" REAL NOT NULL,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
