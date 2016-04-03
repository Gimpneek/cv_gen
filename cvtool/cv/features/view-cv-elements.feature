@fixtures
Feature: View CV Elements
  As A Job Hunter
  In Order to see the skills, experience, education and profile elements I've entered into the system
  I Want to see a list of these elements

  Scenario: List skills
    When I view the listing of skills
    Then I should be able to see the skills I've added to the system

  Scenario: View skill from list
    Given I view the listing of skills
    When I click on a skill in the list
    Then I should be able to edit the skill

  Scenario: Add skill
    Given I view the listing of skills
    When I click on the "Add skill" button
    Then I should be taken to a form to add a skill

  Scenario: List experience
    When I view the listing of experiences
    Then I should be able to see the experiences I've added to the system

  Scenario: View experience from list
    Given I view the listing of experiences
    When I click on a experience element in the list
    Then I should be able to edit the experience

  Scenario: Add experience
    Given I view the listing of experiences
    When I click on the "Add experience" button
    Then I should be taken to a form to add a experience

  Scenario: List education
    When I view the listing of educations
    Then I should be able to see the educations I've added to the system

  Scenario: View education from list
    Given I view the listing of educations
    When I click on a education element in the list
    Then I should be able to edit the education

  Scenario: Add education
    Given I view the listing of educations
    When I click on the "Add education" button
    Then I should be taken to a form to add a education

  Scenario: List profiles
    When I view the listing of profiles
    Then I should be able to see the profiles I've added to the system

  Scenario: View profiles from list
    Given I view the listing of profiles
    When I click on a profile in the list
    Then I should be able to edit the profile

  Scenario: Add profile
    Given I view the listing of profiles
    When I click on the "Add profile" button
    Then I should be taken to a form to add a profile