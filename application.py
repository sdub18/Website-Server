##
##  application.py
##  Website-Server
##
##  Created by Sam DuBois on 6/23/20.
##  Copyright © 2020 Samuel DuBois. All rights reserved.
##

from flask import Flask, request, jsonify

# MARK: Instantiate Our Server
server = Flask(__name__)

# MARK: Internal Routes
@server.route('/', methods=['GET'])
def welcomeClient():
    return jsonify({'message': 'Welcome to my Website Backend'})

# MARK: Run Server
if __name__ == '__main__':
    server.run()
