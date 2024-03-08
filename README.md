# rtma-js

Javascript rtma/websocket client.

1. Install the latest [pyrtma](https://github.com/pitt-rnel/pyrtma/):

    `pip install pyrtma`

2. Write and build message defs for python and js (see [pyrtma documentation](https://pyrtma.readthedocs.io/)):

    `python -m pyrtma.compile -i message_defs.yaml --py --js`

3. Run Message Manager:

    `python -m pyrtma.manager`

4. Run Web Manager:

    `python -m pyrtma.web_manager -d message_defs.py`

5. Import and call rtma-js client from your javascript web app


## Installing as dependency
To install rtma-js as a npm package into your react project:

1. Clone this repo

    `git clone github.com/pitt-rnel/rtma-js`

2. cd into your project directory

3. NPM install
   
   Use a relative or absolute path to this rtma-js repo, e.g.
   
   `npm install ../../rtma-js`

4. Using RTMAClient

    ```js
    import { RTMA } from "climber_message";
    import { RTMAClient } from "rtma-js";

    export default function Main() {    
        const server = "127.0.0.1";
        const port = 5678;
        const module_id = 0;

        const client = new RTMAClient(server, port, module_id);

        //install handlers before connecting
        client.on_connect = () => {
            // subscribe to an array of RTMA messages
            client.subscribe([RTMA.MT.EXAMPLE_MSG]);
        }

        client.on_message = (msg) => {
            // your logic here
            if (msg.header.msg_type === RTMA.MT.EXAMPLE_MSG){
                const data = msg.data;
                const reply_msg = RTMA.MDF.EXAMPLE_MSG_REPLY();
                client.send_message(RTMA.MT.EXAMPLE_MSG_REPLY, reply_msg);
            }
        }

        client.connect();

    }      
    ```
