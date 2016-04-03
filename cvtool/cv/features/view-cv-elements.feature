Feature: View CV Elements
  As A Job Hunter
  In Order to see the skills, experience, education and profile elements I've entered into the system
  I Want to see a list of these elements

  Scenario: List skills
    When I view the listing of skills
    Then I should be able to see the skills I've added to the system

  Scenario: View skill from list
    Given I am viewing the list of skills
    When I click on a skill in the list
    Then I should be able to edit the skill

  Scenario: Add skill
    Given I am viewing the list of skills
    When I click on the "Add skill" button
    Then I should be taken to a form to add a skill

  Scenario: List experience
    When I view the listing of experience elements
    Then I should be able to see the experience elements I've added to the system

  Scenario: View experience from list
    Given I am viewing the list of experience elements
    When I click on a experience element in the list
    Then I should be able to edit the experience

  Scenario: Add experience
    Given I am viewing the list of experience elements
    When I click on the "Add experience" button
    Then I should be taken to a form to add an experience

  Scenario: List education
    When I view the listing of education elements
    Then I should be able to see the education elements I've added to the system

  Scenario: View education from list
    Given I am viewing the list of education elements
    When I click on a education element in the list
    Then I should be able to edit the education

  Scenario: Add education
    Given I am viewing the list of education elements
    When I click on the "Add education" button
    Then I should be taken to a form to add an education

  Scenario: List profiles
    When I view the listing of profiles
    Then I should be able to see the profiles I've added to the system

  Scenario: View profiles from list
    Given I am viewing the list of profiles
    When I click on a profile in the list
    Then I should be able to edit the profile

  Scenario: Add profile
    Given I am viewing the list of profiles
    When I click on the "Add profile" button
    Then I should be taken to a form to add a profile