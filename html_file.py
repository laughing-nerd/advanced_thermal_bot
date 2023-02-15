html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="./style/style.css" /> -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <style>
      * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
      }

      .remote-container {
        width: 100vw;
        min-height: 100vh;
        background-color: rgb(0, 0, 0);

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
      }

      .remote {
        width: 300px;
        height: 300px;
        border-radius: 10px;
        background-color: transparent;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        overflow: hidden;
      }

      .remote-switches {
        width: 80%;
        height: 80%;
        background-color: transparent;
        border-radius: 50%;
        background: #000000;

        position: relative;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 0px 42px 0px rgba(255, 0, 0, 1);
      }

      .right {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        right: 0px;
        top: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .right:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .left {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        left: 0px;
        top: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .left:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .up {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        top: 3px;
        left: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .up:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      .down {
        width: 50px;
        height: 50px;
        font-size: 44px !important;

        color: white;
        background: transparent;
        position: absolute;
        bottom: 0px;
        left: 40%;

        /* border: 1px red solid; */
        border-radius: 50%;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
      }

      .down:hover {
        background-color: rgba(239, 117, 117, 0.352);
      }

      button {
        border: transparent;
      }

      .power-on {
        width: 120px !important;
        height: 120px !important;
        border-radius: 50%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background-color: rgba(30, 30, 30, 0.779);
        /* background-color: red; */
        color: white;

        box-shadow: 0px 0px 53px 0px rgba(255, 0, 0, 1);

        font-size: 18px;
        font-weight: 600;
        border: none;
      }

      .on-of-status {
        width: 120px !important;
        height: 120px !important;
        border-radius: 50%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        background-color: rgba(30, 30, 30, 0.779);
        color: white;

        box-shadow: 1px 5px 42px -3px rgba(0, 170, 255, 1);

        font-size: 18px;
        font-weight: 600;
        border: none;
      }

      @media only screen and (max-width: 600px) {
        .remote {
          width: 280px;
          height: 280px;
        }
      }
    </style>
  </head>
  <body>
    <div class="remote-container">
      <form class="remote">
        <div class="remote-switches">
          <button
            class="up fa fa-caret-up"
            name="button"
            value="forward"
            type="submit"
          ></button>

          <button
            class="left fa fa-caret-left"
            name="button"
            value="left"
            type="submit"
          ></button>

          <button
            class="right fa fa-caret-right"
            name="button"
            value="right"
            type="submit"
          ></button>

          <button
            class="down fa fa-caret-down"
            name="button"
            value="backward"
            type="submit"
          ></button>

          <button class="power-on" name="button" value="stop" type="submit">
            stop
          </button>
        </div>
      </form>
    </div>
  </body>
</html>

 """