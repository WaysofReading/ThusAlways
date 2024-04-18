label hero1_path:

    menu:
        "Duty":
            call hero1_duty
        "Happiness":
            call hero1_happiness
        "Family":
            call hero1_family
    return

    label hero1_duty:
        menu:
            'It\'s a calling, not a certainty':
                call hero1_duty_calling
            'This is a sacred mission, indeed':
                call hero1_duty_sacred_mission
            'Do you really believe you\'re special?':
                call hero1_duty_special
        return

        label hero1_duty_calling:
            hermit 'It\'s a calling, not a certainty'
            hero1 'Yeah, I guess so. But it\'s a prophecy, isn\'t it?'
            $ hero1_score = hero1_score + 1
            return

        label hero1_duty_sacred_mission:
            hermit 'This is a sacred mission, indeed'
            hero1 'I think so, too'
            $ hero1_score = hero1_score + 0
            return

        label hero1_duty_special:
            hermit 'Do you really believe you\'re special?'
            hero1 'I was chosen to save the world!'
            $ hero1_score = hero1_score - 1
            return

    label hero1_happiness:
        menu:
            'Happiness involves others':
                call hero1_happiness_others
            'Happiness is very personal':
                call hero1_happiness_personal
            'Happiness is fleeting':
                call hero1_happiness_fleeting
        return

        label hero1_happiness_others:
            hermit '"Happiness involves others"'
            hero1 '"Ultimate happiness is when everyone is happy"'
            $ hero1_score = hero1_score + 1
            return

        label hero1_happiness_personal:
            hermit '"Happiness is very personal"'
            hero1 '"Not everyone will like the same things"'
            $ hero1_score = hero1_score + 0
            return

        label hero1_happiness_fleeting:
            hermit '"Happiness is fleeting"'
            hero1 '"Well, I was happy before you said that..."'
            $ hero1_score = hero1_score - 1
            return

    label hero1_family:
        menu:
            'Family is a choice':
                call hero1_family_choice
            'Family is blood':
                call hero1_family_blood
            'Family is a hindrance':
                call hero1_family_hindrance
        return

        label hero1_family_others:
            hermit '"Family is a choice"'
            hero1 '"Like my friends"'
            $ hero1_score = hero1_score + 1
            return

        label hero1_family_blood:
            hermit '"Family is blood"'
            hero1 '"I guess that makes sense."'
            $ hero1_score = hero1_score + 0
            return

        label hero1_family_hindrance:
            hermit '"Family is a hindrance"'
            hero1 '"My family is why I\'m here."'
            $ hero1_score = hero1_score - 1
            return

label hero2_path:

    menu:
        "Duty":
            call hero2_morality
        "Happiness":
            call hero2_knowledge
        "Family":
            call hero2_family
    return

    label hero2_morality:
        menu:
            'How do you want to be remembered?':
                call hero2_morality_remembered
            'It really depends on the circumstance':
                call hero2_morality_circumstance
            'Morals are false things of a dead society':
                call hero2_morality_false
        return

        label hero2_morality_remembered:
            hermit '"How do you want to be remembered?"'
            hero2 '"A good point... though that could be what brings about one\'s end."'
            $ hero2_score = hero2_score + 1
            return

        label hero2_morality_circumstance:
            hermit '"It really depends on the circumstance"'
            hero2 '"I suppose so. But is survival always the right choice..?"'
            $ hero2_score = hero2_score + 0
            return

        label hero2_morality_false:
            hermit '"Morals are false things of a dead society"'
            hero2 '"That kind of thinking is why my family is dead."'
            $ hero2_score = hero2_score - 1
            return

    label hero2_knowledge:
        menu:
            'No amount of harm is acceptable, but we can still learn from our mistakes':
                call hero2_knowledge_learn_from_mistakes
            'We should try to avoid causing harm in the pursuit of knowledge':
                call hero2_knowledge_avoid_harm
            'Everybody suffers whether we learn something or not':
                call hero2_knowledge_everybody_suffers
        return

        label hero2_knowledge_learn_from_mistakes:
            hermit '"No amount of harm is acceptable, but we can still learn from our mistakes"'
            hero2 '"Ultimate happiness is when everyone is happy"'
            $ hero2_score = hero2_score + 1
            return

        label hero2_knowledge_avoid_harm:
            hermit '"We should try to avoid causing harm in the pursuit of knowledge"'
            hero2 '"Well, that\'s obvious. I was asking if the knowledge learned from suffering still has value, or if it\'s tainted at its core."'
            $ hero2_score = hero2_score + 0
            return

        label hero2_knowledge_everybody_suffers:
            hermit '"Everybody suffers whether we learn something or not"'
            hero2 '"So everything just suffers pointlessly?"'
            $ hero2_score = hero2_score - 1
            return

    label hero2_family:
        menu:
            'Maybe, but they\'re not common.':
                call hero2_relationships_not_common
            'Of course there is. Love is unconditional.':
                call hero2_relationships_love_is_unconditional
            'Everything has a condition.':
                call hero2_relationships_everything_is_conditional
        return

        label hero2_relationships_not_common:
            hermit '"Maybe, but they\'re not common."'
            hero2 '"... What would one look like..?"'
            $ hero2_score = hero2_score + 1
            return

        label hero2_relationships_love_is_unconditional:
            hermit '"Of course there is. Love is unconditional."'
            hero2 '"All love? I somehow doubt that."'
            $ hero2_score = hero2_score + 0
            return

        label hero2_relationships_everything_is_conditional:
            hermit '"Everything has a condition."'
            hero2 '"Maybe so. But... I would have liked to have thought otherwise."'
            $ hero2_score = hero2_score - 1
            return

label hero3_path:

    menu:
        "Duty":
            call hero3_life_value
        "Happiness":
            call hero3_preservation
        "Family":
            call hero3_flaws
    return

    label hero3_life_value:
        menu:
            'It\'s what you choose it to be.':
                call hero3_life_value_choice
            'All life is priceless':
                call hero3_life_value_priceless
            'Life is meaningless regardless of its form':
                call hero3_life_value_meaningless
        return

        label hero3_life_value_choice:
            hermit '"It\'s what you choose it to be."'
            hero3 '"That\'s a lot of power to put in one person\'s hand."'
            $ hero3_score = hero3_score + 1
            return

        label hero3_life_value_priceless:
            hermit '"All life is priceless"'
            hero3 '"In the cosmic scheme of things, maybe..."'
            $ hero3_score = hero3_score + 0
            return

        label hero3_life_value_meaningless:
            hermit '"Life is meaningless regardless of its form"'
            hero3 '"... That\'s not promising."'
            $ hero3_score = hero3_score - 1
            return

    label hero3_preservation:
        menu:
            '"To preserve memories of ourselves and the people we cared for"':
                call hero3_preservation_memories
            'To record history, so we can remember our roots and avoid repeating the past':
                call hero3_preservation_history
            '"To remember our accomplishments and triumphs over our foes."':
                call hero3_preservation_triumph
        return

        label hero3_preservation_memories:
            hermit '"To preserve memories of ourselves and the people we cared for"'
            hero3 '"... That\'s... one way to look at it."'
            $ hero3_score = hero3_score + 1
            return

        label hero3_preservation_history:
            hermit '"To record history, so we can remember our roots and avoid repeating the past"'
            hero3 '"Have we really learned anything though?"'
            $ hero3_score = hero3_score + 0
            return

        label hero3_preservation_triumph:
            hermit '"To remember our accomplishments and triumphs over our foes."'
            hero3 '"So it\'s all just one big contest?"'
            $ hero3_score = hero3_score - 1
            return

    label hero3_flaws:
        menu:
            'Our flaws are meant to be overcome, not define us.':
                call hero3_flaws_overcome
            'There are other things that define us aside from flaws':
                call hero3_flaws_other_things
            'Yes. Our flaws are as ingrained as our DNA':
                call hero3_flaws_ingrained
        return

        label hero3_flaws_overcome:
            hermit '"Our flaws are meant to be overcome, not define us."'
            hero3 '"That\'s a long road to travel."'
            $ hero3_score = hero3_score + 1
            return

        label hero3_flaws_other_things:
            hermit '"There are other things that define us aside from flaws."'
            hero3 '"It feels like the flaws outweigh whatever might be good."'
            $ hero3_score = hero3_score + 0
            return

        label hero3_flaws_ingrained:
            hermit '"Yes. Our flaws are as ingrained as our DNA."'
            hero3 '"Even for me, that\'s absurdly pessimistic."'
            $ hero3_score = hero3_score - 1
            return
