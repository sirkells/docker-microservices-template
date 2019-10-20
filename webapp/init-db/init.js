db.createUser({
  user: "user",
  pwd: "secretPassword",
  roles: [{ role: "readWrite", db: "projectfinder" }]
});

db.itproject.insert({
  title: "Python Developer"
});
