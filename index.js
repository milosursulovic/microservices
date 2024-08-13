import UsersService from "./services/user.service.js";

async function startApp() {
  await UsersService.start();

  try {
    const newUser = await UsersService.call("user.createUser", {
      username: "john",
      email: "john@email.com",
    });
    console.log("New user created: ", newUser);
    const users = await UsersService.call("user.getUsers");
    console.log("All users: ", users);
  } catch (error) {
    console.log("Error: ", error);
  } finally {
    await UsersService.stop();
  }
}

startApp();
