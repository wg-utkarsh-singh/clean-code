function connectDatabase() {
  const didConnect = database.connect();
  if (didConnect) {
    return true;
  } else {
    return false;
  }
}

function determineSupportAgent(ticket) {
  if (ticket.requestType === "unknown") {
    return findStandardAgent();
  }
  return findAgentByRequestType(ticket.requestType);
}

function isValid(email, password) {
  if (!email.includes("@") || password.length < 7) {
    return false;
  }
  return true;
}

function initApp() {
  let status;

  status = connectDatabase();
  if (!status) {
    console.log("Could not connect to database.");
  }
}
