Feature: Add education
  As A Job Hunter
  In Order to add my education
  I Want to be able to be add the institution I studied at, the timeframe and the courses and marks I took

  Scenario: Add institution studied at
    When I add a new education
    Then I should be able to add the name of the institution I studied at

  Scenario: Add timeframe for education
    When I add a new education
    Then I should be able to add the date I started the education
    And I should be able to add the date I finished the education

  Scenario: Add minimal information for education
    When I add a new education
    Then I should be able to submit the form by only adding:
      | information |
      | institution |
      | start date  |

  Scenario: Add existing course for education
    When I add a new education
    Then I should be able to select an existing course I took as part of the education

  Scenario: Add new course for education
    When I add a new education
    And I want to add a course to the education
    But the course is not created yet
    Then I should be able to create the course
    And assign it to the education