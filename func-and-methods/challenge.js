function isValidEmail(email) {
  return email && email.includes("@");
}

function isValidPassword(password) {
  return password && password.trim != "";
}

function createrUser(email, password) {
  if (isValidEmail(email) && isValidPassword(password))
    return { email, password };
}

function addUser(email, password) {
  let user = createrUser(email, password);
  database.insert(user);
}
