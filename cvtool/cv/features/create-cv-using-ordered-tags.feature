Feature: Create CV using ordered tags
  As A Job Hunter
  In Order to have a customised CV for each job I apply for
  I Want to be able to generate a CV using an ordered list of tags which will contain information tailored towards those tags

  Scenario: Add tags to list
    When I create a new CV
    Then I should be able to select existing tags to add to the list

  Scenario: Generate CV with information for tags
    Given I have the following skills:
      | skill   | tag          |
      | Skill 1 | Tag 1        |
      | Skill 2 | Tag 1, Tag 2 |
      | Skill 3 | Tag 3        |
      | Skill 4 | Tag 2        |
    When I generate the CV using the following order:
      | order |
      | Tag 1 |
      | Tag 2 |
    Then I should see the skills in this order:
      | order   |
      | Skill 1 |
      | Skill 2 |
      | Skill 4 |
      | Skill 3 |