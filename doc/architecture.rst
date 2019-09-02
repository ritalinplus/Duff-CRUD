======================
Architecture
======================

In this section the system architecture will by explained.
The system is based in a docker container architecture, specifically 2 container:

1. dg01 container: based in python container, contains the system's core, including validators, serializers and user interface.

2. ps01 container: based in postgresql container, it store client data.

.. image:: _images/architecture.png
    :align: center

System Core
#############

In this section all components of the system's core will be explained.


System Validators
======================

All field including in the forms used for store client data are validating following this rules.

* Name: only can include letters.
* Surname: only can include letters.
* IBAN account: checks valid country-code and checksum digits.


System User Interface
======================

Created using DRF default templates to navigate for the browsable API and a custom login view to allow
sing in using a google account.

.. image:: _images/api_root.png

System API Endpoints
======================

Created using DRF, in this section the different endpoints and operations allowed will be explained.

**Clients**

==========   =========================   ================================
Operation    Endpoint                    Description
==========   =========================   ================================
GET          /v1/clients                 Retrieves all stored data
GET          /v1/clients/[client-id]     Retrieves client stored data
POST         /v1/clients                 Inserts client stored data
DELETE       /v1/clients/[client-id]     Deletes client stored data
PUT          /v1/clients/[client-id]     Updates client stored data
PATCH        /v1/clients/[client-id]     Updates client stored data
==========   =========================   ================================


System Database
##################

In this section the system's database will be explained.

Database Models
======================

**Client Model**

==========   =========================   ================================
Field        Type                        Description
==========   =========================   ================================
name         CharField                   Client name
surname      CharField                   Client surname
iban         CharField                   Client IBAN Account
==========   =========================   ================================


**Owner Model**

==========   ============================   ================================
Field        Type                           Description
==========   ============================   ================================
owner        ForeignKey(AUTH_USER_MODEL)    Django User
==========   ============================   ================================
