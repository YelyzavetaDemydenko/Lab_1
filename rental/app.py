from flask import Flask, render_template, request, redirect, url_for, session

import sys
sys.path.append(".")
from Lab_1 import House, Tenant, Landlord, Contract

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

list_of_houses_ = []
list_of_landlords_ = []
list_of_tenants_ = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        name = request.form['name']
        account_type = request.form['account']
        if account_type == "Орендатор":
            return redirect(url_for('tenant_login', name=name, account_type = account_type))
        else:
            return redirect(url_for('landlord_login', name=name, account_type = account_type))


@app.route("/houses")
def houses():
    return render_template("houses.html", landlords_ = list_of_landlords_)


@app.route("/tenant_login")
def tenant_login():
    name = request.args.get('name')
    account_type = request.args.get('account_type')
    flag = 0
    for tenant in list_of_tenants_:
        if tenant.name == name:
            flag = 1
            tenant_ = tenant
            break
    if not flag:
        list_of_tenants_.append(Tenant(name))
        tenant_ = list_of_tenants_[-1]

    session["tenant_name"] = tenant_.name
    return render_template("tenant_login.html", account_type = account_type, tenant_ = tenant_)


@app.route("/tenant")
def tenant():
    tenant_name = session.get('tenant_name')
    for tenant in list_of_tenants_:
        if tenant.name == tenant_name:
            tenant_ = tenant
            break
    session["tenant_name"] = tenant_.name
    return render_template("tenant.html", tenant_ = tenant_)


@app.route("/tenant_name", methods = ['GET', 'POST'])
def tenant_name():
    tenant_name = session.get('tenant_name')
    for tenant in list_of_tenants_:
        if tenant.name == tenant_name:
            tenant_ = tenant
            break
    
    if request.method == "GET":
        return render_template("tenant_name.html")
    elif request.method == "POST":
        name = request.form["name"]
        tenant_.name = name
    session["tenant_name"] = tenant_.name
    return redirect(url_for("tenant"))


@app.route("/tenant_houses")
def tenant_houses():
    tenant_name = session.get('tenant_name')
    for tenant in list_of_tenants_:
        if tenant.name == tenant_name:
            tenant_ = tenant
            break
    session["tenant_name"] = tenant_.name
    return render_template("tenant_houses.html", landlords_ = list_of_landlords_)


@app.route("/landlord_login")
def landlord_login():
    name = request.args.get('name')
    account_type = request.args.get('account_type')
    flag = 0
    for landlord in list_of_landlords_:
        if landlord.name == name:
            flag = 1
            landlord_ = landlord
            break
    if not flag:
        list_of_landlords_.append(Landlord(name))
        landlord_ = list_of_landlords_[-1]

    session["landlord_name"] = landlord_.name
    return render_template("landlord_login.html", account_type = account_type, landlord_ = landlord_)


@app.route("/landlord")
def landlord():
    landlord_name = session.get('landlord_name')
    for landlord in list_of_landlords_:
        if landlord.name == landlord_name:
            landlord_ = landlord
            break
    session["landlord_name"] = landlord_.name
    return render_template("landlord.html", landlord_ = landlord_)


@app.route("/landlord_name", methods = ['GET', 'POST'])
def landlord_name():
    landlord_name = session.get('landlord_name')
    for landlord in list_of_landlords_:
        if landlord.name == landlord_name:
            landlord_ = landlord
            break
    
    if request.method == "GET":
        return render_template("landlord_name.html")
    elif request.method == "POST":
        name = request.form["name"]
        landlord_.name = name
    session["landlord_name"] = landlord_.name
    return redirect(url_for("landlord"))


@app.route('/landlord_houses')
def landlord_houses():
    landlord_name = session.get('landlord_name')
    for landlord in list_of_landlords_:
        if landlord.name == landlord_name:
            landlord_ = landlord
            break
    session["landlord_name"] = landlord_.name
    return render_template("landlord_houses.html", houses_ = landlord_.list_of_houses)


@app.route("/new_house", methods = ['GET', 'POST'])
def new_house():
    landlord_name = session.get('landlord_name')
    for landlord in list_of_landlords_:
        if landlord.name == landlord_name:
            landlord_ = landlord
            break
    session["landlord_name"] = landlord_.name
    if request.method == 'GET':
        return render_template("new_house.html")
    elif request.method == 'POST':
        price = int(request.form['price'])
        new_house_ = House(price)
        landlord_.list_of_houses.append(new_house_)
        list_of_houses_.append(new_house_)
        return redirect(url_for("landlord"))


@app.route('/contract/<landlord_name>/<int:house_number>', methods = ['GET', 'POST'])
def contract(landlord_name, house_number):
    tenant_name = session.get('tenant_name')
    for tenant in list_of_tenants_:
        if tenant.name == tenant_name:
            tenant_ = tenant
            break
    for landlord in list_of_landlords_:
        if landlord.name == landlord_name:
            landlord_ = landlord
            break
    for house in landlord_.list_of_houses:
        if house.number == house_number:
            house_ = house
    if request.method == "GET":
        return render_template("contract.html", tenant_name = tenant_.name, landlord_name = landlord.name, house_number = house_.number)
    elif request.method == "POST":
            start_date = str(request.form['start_date'])
            end_date = str(request.form['end_date'])
            Contract(house_, landlord_, tenant_, start_date, end_date)
    session["tenant_name"] = tenant_.name
    return redirect(url_for("contract_details"))

@app.route("/contract_details")
def contract_details():
    tenant_name = session.get('tenant_name')
    for tenant in list_of_tenants_:
        if tenant.name == tenant_name:
            tenant_ = tenant
            break
    session["tenant_name"] = tenant_.name

    contract_ = Contract.list_of_contracts[-1]
    return render_template("contract_details.html", contract_ = contract_)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
