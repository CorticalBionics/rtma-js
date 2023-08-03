# rtma-js

Javascript rtma/websocket client.

Here are the commands to get a local setup of rtma running in my dev-yaml branch:

1. Download the pyrtma repo:

    `git clone github.com/pitt-rnel/pyrtma`

2. Checkout the dev-yaml branch for now:

    `git checkout dev-yaml`

3. Build a python env:

     `conda env create -n pyrtma`

4. Activate the newly created python environment:

    `conda activate pyrtma`

5. Go to the pyrtma directory and install pyrtma:

     `pip install -e .`

6. Build the test copy of climber_config in the testing folder:

    `python -m pyrtma.compile -i msg_defs/climber_config.yaml --py --c --mat --js`

7. In one console, activate the env and run message manager:

     ```
     conda activate pyrtma
     python -m pyrtma.manager -a 127.0.0.1 -T
     ```

8. In another console, activate the env and run the websocket manager:

    ```
    conda activate pyrtma
    python -m pyrtma.web_manager --host 127.0.0.1 --port 5678 --defs ./defs/climber_config.py
    ```

9. In another console, run the test web server in this repo to serve up the examples:

    ```
    cd rtma-js
    python test_webserver.py
    ```

10. Open a browser and go to the example page: ```localhost:8000/example/echo/index.html```


## Installing as dependency
To install rtma-js as a npm package into your react project:

1. Clone this repo

    `git clone github.com/pitt-rnel/rtma-js`

2. cd into your React project directory (not the Github repo but the actual React project folder)

3. NPM install
   
   For example if your SpikeViewer repo and the rtma-js repo are in the same dirctory, run
   
   `npm install ../../rtma-js`

4. Using RTMAClient

    ```
    import { RTMA } from "climber_message";
    import { RTMAClient } from "rtma-js";

    export default function Main() {    
        let server = "127.0.0.1";
        let port = 5678;
        let module_id = 0;

        let client = new RTMAClient(server, port, module_id);

        client.init();
        client.on_connect = () => {
            // subscribe to RTMA messages
            client.subscribe(RTMA.MT.FILTERED_SPIKE);
        }

        client.on_message = (msg) => {
            // your logic here
        }

    }      
    ```
