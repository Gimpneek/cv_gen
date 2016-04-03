Feature: Add experience
  As A Job Hunter
  In Order to add my previous or current jobs
  I Want to be able to add the company, position, timeframe, responsibilities and projects for that job

  Scenario: Add company worked for
    When I add a new job
    Then I should be able to add the company I worked for

  Scenario: Add position held in job
    When I add a new job
    Then I should be able to add the position I held in the job

  Scenario: Add timeframe for job
    When I add a new job
    Then I should be able to add the date I started the job
    And I should be able to add the date I ended the job if applicable

  Scenario: Add minimal information for job
    When I add a new job
    Then I should be able to submit the form by only adding:
      | information |
      | company     |
      | position    |
      | start date  |

  Scenario: Add existing responsibility for job
    When I add a new job
    Then I should be able to select an existing responsibility for the job

  Scenario: Add new responsibility for job
    When I add a new job
    And I want to add a responsibility for the job
    But the responsibility is not created yet
    Then I should be able to create the responsibility
    And assign it to the job

  Scenario: Add existing project for job
    When I add a new job
    Then I should be able to select an existing project for the job

  Scenario: Add new project for job
    When I add a new job
    And I want to add a project for the job
    But the project is not created yet
    Then I should be able to create the project
    And assign it to the job