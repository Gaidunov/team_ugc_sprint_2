
// Create collection with a $jsonschema

conn = new Mongo();
db = conn.getDB("movies");

db.createCollection("reviews", {
    validator: {$jsonSchema: {
        required: [ "text", "movie_id", "author_name", "author_id", "review_id", "date"],
         bsonType: "object",
            properties: {
                movie_id:{
                bsonType: "string"
                },
                review_id:{
                    bsonType: "int"
                },
                text: {
                    bsonType: "string"
                },
                author_name : {
                    bsonType: "string"
                },
                author_id : {
                    bsonType: "string"
                },
                date:{
                    bsonType: "date" 
                } 
        }}}})

db.reviews.createIndex( { "review_id": 1 })

db.createCollection("likes", {
    validator: {$jsonSchema:{
        bsonType: "object",
        required: [ "user_id", "review_id", "date"],
        properties: {
            user_id: {
                bsonType: "string"
            },
            review_id:{
                bsonType: "int"
            },
            date:{
                bsonType: "date" 
            }
        }
    }}
})


db.likes.createIndex( { "review_id":1})


