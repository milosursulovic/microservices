import UsersService from "./services/user.service.js";
import EmailService from "./services/email.service.js";
import AuthService from "./services/auth.service.js";

async function startApp() {
  await UsersService.start();
  await EmailService.start();
  await AuthService.start();

  try {
    const newUser = await UsersService.call("user.createUser", {
      username: "john",
      email: "john@email.com",
    });
    console.log("New user created: ", newUser);
    const users = await UsersService.call("user.getUsers");
    console.log("All users: ", users);

    const emailResult = await EmailService.call("email.sendEmail", {
      recipient: newUser.email,
      subject: "Welcome to our platform!",
      content: "Thank you for sign up!",
    });
    console.log(emailResult);

    const authResult = await AuthService.call("auth.authUser", {
      username: newUser.username,
      password: "password",
    });
    console.log("Auth result: ", authResult);
  } catch (error) {
    console.log("Error: ", error);
  } finally {
    await UsersService.stop();
    await EmailService.stop();
    await AuthService.stop();
  }
}

startApp();
