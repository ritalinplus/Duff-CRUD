=======================================
Management
=======================================

In this section How to use the system will by explained

Access
##########

To access the system you only need a google account and access to http://localhost:8000 (with the system up)
and Sign in.

.. image:: _images/login.png


when are successfully log in, you will see the API root view and you can start to navigate inside the whole
system

.. image:: _images/api_root.png

then you can choose the desired endpoint (clients) and client list will be shown.

Client List View
##################

Show all client stored in the system. Consists of 2 component.

1. view panel, where results are shown

.. image:: _images/clients_view.png

2. Form panel to introduce data for store new clients.

.. image:: _images/clients_form.png


Basic Operations
###################

In this section system basic operation will be described


Retrieve all clients
============================

In the client view pick in the top blue button (GET).

.. image:: _images/clients_get.png

then the client list are shown in the client's view panel.


Store new clients
============================

Fill the client form with the required data and pick in blue down button (POST).

.. image:: _images/clients_post.png


Update client data
============================

Choose the client you want update and pick in url field.

.. image:: _images/clients_select.png

this show you a new view with a new panel at the bottom, change the required data and click in the
blue button (PUT).

.. image:: _images/clients_put.png

.. note::
    Update it's only allowed if you are the owner of the client.

Delete client data
============================

Choose the client you want delete and pick in url field.

.. image:: _images/clients_select.png

this show you a new view, then click in the red button (DELETE).

.. image:: _images/clients_delete.png

.. note::
    Delete it's only allowed if you are the owner of the client.