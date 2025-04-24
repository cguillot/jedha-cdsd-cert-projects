CREATE TABLE "city" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "latitude" DECIMAL(9,6),
  "longitude" DECIMAL(9,6),
  "created_at" TIMESTAMP DEFAULT (now()),
  "updated_at" TIMESTAMP DEFAULT (now())
);

CREATE TABLE "hotel" (
  "id" int PRIMARY KEY,
  "city_id" int,
  "name" varchar,
  "review_appreciation" varchar,
  "review_score" DECIMAL(10,2),
  "rating_stars" int,
  "description" text,
  "latitude" DECIMAL(9,6),
  "longitude" DECIMAL(9,6),
  "url" varchar,
  "rating_squares" int,
  "created_at" TIMESTAMP DEFAULT (now()),
  "updated_at" TIMESTAMP DEFAULT (now())
);

CREATE TABLE "weather_forecast_score" (
  "city_id" int,
  "score_date" date,
  "temperature" DECIMAL(6,2),
  "min_pop" DECIMAL(6,2),
  "mean_pop" DECIMAL(6,2),
  "max_pop" DECIMAL(6,2),
  "created_at" TIMESTAMP DEFAULT (now()),
  PRIMARY KEY ("city_id", "score_date")
);

ALTER TABLE "hotel" ADD FOREIGN KEY ("city_id") REFERENCES "city" ("id");

ALTER TABLE "weather_forecast_score" ADD FOREIGN KEY ("city_id") REFERENCES "city" ("id");
