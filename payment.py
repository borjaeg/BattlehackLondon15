# Imports
import braintree
from flask import Flask, request

# Braintree configuration
braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    'xzk9p3947gggzsgt',
    'wgp52v9n7stqjd2c',
    'beae8f107b64b387a434dbe4b1686a16'
)

# Start flasks
app = Flask(__name__)

# Functions
@app.route("/client_token", methods=["GET"])
def client_token():
    return braintree.ClientToken.generate({
        "customer_id": a_customer_id
  })

@app.route("/purchases", methods=["POST"])
def create_purchase():
    nonce = request.form["payment_method_nonce"]
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce
    })