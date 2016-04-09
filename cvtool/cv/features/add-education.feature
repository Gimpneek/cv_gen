@fixtures
Feature: Add education
  As A Job Hunter
  In Order to add my education
  I Want to be able to be add the institution I studied at, the timeframe and the courses and marks I took

  Scenario: Add institution studied at
    When I create a new education
    Then I should be able to add the name of the institution I studied at

  Scenario: Add timeframe for education
    When I create a new education
    Then I should be able to add the date I started the education
    And I should be able to add the date I finished the education

  Scenario: Add minimal information for education
    When I create a new education
    Then I should be able to submit the form by only adding:
      | information                              |
      | the name of the institution I studied at |
      | the date I started the education         |
      | a course I took as part of the education |

  Scenario: Validation errors on submit empty form
    Given I create a new education
    When I submit an empty form
    Then I should see validation errors for the following fields:
    | invalid_field                            |
    | the name of the institution I studied at |
    | the date I started the education         |
    | a course I took as part of the education |

  Scenario: Add existing course for education
    When I create a new education
    Then I should be able to assign a course I took as part of the education

#  Scenario: Add new course for education
#    When I add a new education
#    And I want to add a course to the education
#    But the course is not created yet
#    Then I should be able to create the course
#    And assign it to the education

  Scenario: Add existing project for education
    When I create a new education
    Then I should be able to assign a project I did as part of my studies

#  Scenario: Add new project for education
#    When I create a new education
#    And I want to add a project for the education
#    But the project is not created yet
#    Then I should be able to create the project
#    And assign it to the education