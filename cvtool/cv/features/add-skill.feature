@fixtures
Feature: Add skill
  As A Job Hunter
  In Order to add a skill to my CV
  I Want to be able to name it and optionally add metadata so my CV can be generated more accurately for different jobs

  Scenario: Add Name for skill
    When I create a new skill
    Then I should be able to add a name for the skill

  Scenario: Add minimal information for skill
    Given I create a new skill
    Then I should be able to submit the form by only adding:
    | information          |
    | a name for the skill |

  Scenario: Validation errors on submit empty form
    Given I create a new skill
    When I submit an empty form
    Then I should see validation errors for the following fields:
    | invalid_field        |
    | a name for the skill |

#  Scenario: Add existing tag to skill
#    When I create a new skill
#    Then I should be able to assign a tag to the skill

#  Scenario: Add new tag to skill
#    When I create a new skill
#    And I want to add a tag to the skill
#    But the tag is not created yet
#    Then I should be able to create the tag
#    And I should be able to assign a tag to the skill

  Scenario: Add proficiency information to skill
    When I create a new skill
    Then I should be able to select the proficiency I have in that skill

  Scenario: Add information on if skill is current practice
    When I create a new skill
    Then I should be able to select if the skill is current practice or not