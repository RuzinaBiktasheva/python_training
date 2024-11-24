Feature: contact

  Scenario Outline: Add new contact
    Given a contact list
    And a contact with <lastname>, <firstname> and <address>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
      | lastname  | firstname  | address  |
      | lastname1 | firstname1 | address1 |
      | lastname2 | firstname2 | address2 |

  Scenario: Delete contact
    Given a contact list
    And random contact
    When I delete the contact to the list
    Then  the new contact list is equal to the old list with the deleted contact


  Scenario Outline: Modification contact
    Given a contact list
    And random contact
    When I modification the contact to the list with <lastname>, <firstname> and <address>
    Then the new contact list is equal to the old list with the modification contact

    Examples:
      | lastname  | firstname  | address  |
      | lastname_modification | firstname_modification | address_modification |