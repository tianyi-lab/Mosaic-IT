MAX_INSTRUCTION_NUMBER = 50

################################################
# DEFINE TAGS
################################################

DIGITS_TAG_LIST = [
    # '',
    '{i}',
    '({i})', 
    '[{i}]', 
    '<{i}>',
    '<<{i}>>',
    '### {i}',
    '## {i}',
    '##{i}##',
    '|{i}|',
    '||{i}||',
]

DIGITS_PUNC_LIST = [
    ' ',
    '.', 
    ':', 
]

BEGIN_END_TAG_PUNC_LIST = [
    # '{text} ',
    '({text})', 
    '[{text}]', 
    '<{text}>',
    '<<{text}>>',
    '|{text}|',
    '[|{text}|]',
    '<|{text}|>',
    '||{text}||',
    '|-|{text}|-|',
    '#{text}|#',
    '###{text}#',
    '##{text}#',
    '\{text}\\',
    '\{text}/',
    '/{text}\\',
    '*{text}*', 
    '**{text}**', 
    '***{text}***', 
    '***{text}*', 
    '**{text}*', 
    '"{text}"', 
    '@{text}@', 
    '@@{text}@@', 
    '@@@{text}@', 
    '${text}$', 
    '$${text}$$', 
    '$$${text}$', 
]

BEGIN_END_TEXT_LIST = [
    ('BEGAIN','END'),
    ('START','END'),
    ('RESPONSE','END'),
    ('RESPONSE','END OF RESPONSE'),
    ('OPEN', 'CLOSE'),
    ('OPEN RESPONSE', 'CLOSE'),
    ('INITIATE', 'TERMINATE'),
    ('ENTRY', 'EXIT'),
    ('LAUNCH', 'CONCLUDE'),
    ('COMMENCE', 'COMPLETE'),
    ('START POINT', 'END POINT'),
    ('ORIGIN', 'DESTINATION'),
    ('INTRODUCTION', 'CONCLUSION'),
    ('KICKOFF', 'WRAP UP'),
    ('RES_START', 'RES_END'),
    ('RES_BEGIN', 'RES_END'),
    ('RES', '/RES'),
]

FORMAT_INSTRUCTION_INTERVAL_TAG_LIST = [
    '\n',
    '\n\n',
]

################################################
# FORMAT VERSION
################################################

FORMAT_META_INSTRUCTION_LIST = [
    """Respond to these instructions in the format of {begin_tag}response{end_tag} for each instruction.""",
    """For each instruction given, provide a response framed by {begin_tag} at the start and {end_tag} at the end.""",
    """Each instruction should be answered using the format {begin_tag}response{end_tag}.""",
    """Answer each question by formatting your response between {begin_tag} and {end_tag}.""",
    """Please frame your response to each of these instructions using {begin_tag} at the beginning and {end_tag} at the conclusion.""",
    """Use the {begin_tag}response{end_tag} format to reply to every instruction presented.""",
    """Every instruction must be responded to within the confines of {begin_tag} and {end_tag}.""",
    """Format your answers to these instructions with a {begin_tag} before and an {end_tag} after each response.""",
    """Reply to each of the following instructions by enclosing your response between {begin_tag} and {end_tag}.""",
    """For responding to these instructions, enclose your reply between {begin_tag} and {end_tag}.""",
    """Provide your response to each instruction by starting with {begin_tag} and ending with {end_tag}.""",
    """Encapsulate your reply to each command between {begin_tag} and {end_tag}.""",
    """Begin and conclude your responses to these directions with {begin_tag} and {end_tag}, respectively.""",
    """Surround your answers to these guidelines with {begin_tag} at the start and {end_tag} at the finish.""",
    """Ensure each response to the instructions is bookended by {begin_tag} and {end_tag}.""",
    """Wrap your reactions to each prompt with {begin_tag} at the beginning and {end_tag} at the end.""",
    """Apply the {begin_tag} and {end_tag} format to frame your responses to the given instructions.""",
    """Use {begin_tag} to open and {end_tag} to close your answer to each instruction provided.""",
    """Frame each response to the instructions using {begin_tag} to initiate and {end_tag} to conclude""",
    """Begin with {begin_tag} and end with {end_tag} when responding to each of these instructions.""",
    """For each instruction, enclose your reply within {begin_tag} and {end_tag}.""",
    """Respond to each of these commands by starting with {begin_tag} and finishing with {end_tag}.""",
    """Each response should be entered with {begin_tag} at the beginning and {end_tag} at the end.""",
    """Craft your responses to these instructions by using {begin_tag} before and {end_tag} after your reply.""",
    """Format each reply to these guidelines between {begin_tag} and {end_tag}.""",
    """Your responses should be framed using {begin_tag} at the start and {end_tag} at the close.""",
    """For each of these instructions, your reply should start with {begin_tag} and end with {end_tag}.""",
    """Encase each answer to the instructions with {begin_tag} leading and {end_tag} following.""",
    """In replying to each instruction, use {begin_tag} to begin and {end_tag} to end your response.""",
    """Each instruction should be answered by surrounding your text with {begin_tag} and {end_tag}.""",
]

FORMAT_META_INSTRUCTION_NO_LIST = [
    """Respond to these instructions.""",
    """For each instruction given, provide a response.""",
    """Answer each question.""",
    """Reply to every instruction presented.""",
    """Reply to each of the following instructions.""",
    """Provide your response to each instruction.""",
    """Respond to each of these commands.""",
]

FORMAT_OVERALL_INSTRUCTION_LIST = [
    """{meta_instruction}\n{instruction_all}""",
    """{instruction_all}\n{meta_instruction}""",
    """{meta_instruction}\n\n{instruction_all}""",
    """{instruction_all}\n\n{meta_instruction}""",
]

################################################
# ORDER VERSION
################################################

ORDER_META_INSTRUCTION_FIX_LIST = [
    """Respond in the order of {}.""",
    """Structure your response in the order indicated here: {}.""",
    """Please ensure your replies follow the specified sequence: {}.""",
    """Please follow the designated sequence {} when formulating your response.""",
    """Please align your replies precisely with the sequence indicated: {}.""",
    """Format your response in accordance with the sequence: {}.""",
    """Your replies must correspond to the exact sequence described: {}.""",
]

ORDER_META_INSTRUCTION_REVERSE_LIST = [
    """Respond in the reverse order.""",
    """Reverse the order of your replies.""",
    """Begin response with the last instruction, go backwards.""",
    """Start response with the final instuction, proceed in reverse.""",
    """Reverse the instruction order in your response, starting at the end.""",
    """Start with the final instruction and discuss each prior one in reverse.""",
    """Begin with responding the last instruction and work your way to the first.""",
]

ORDER_META_INSTRUCTION_ALPHA_LIST = [
    """Respond in the alphabetical order of the first letter of instruction.""",
    """Respond in ascending alphabetical order by the first character of each instruction."""
    """List your responses by the alphabetical order of the initial letter in each instruction."""
    """Structure your replies in alignment with the alphabetical order determined by the first letter of each instruction."""
    """Reply in a sequence that respects the alphabetical order of the first letter of each directive."""
    """Provide your answers in an order that reflects the alphabetical precedence of each instruction's starting letter."""
    """Your responses should be prioritized by the alphabetical order of the initial letter in each instruction."""
    """Ensure responses are ordered by the initial letter of each instruction, following the alphabetical order."""
]

ORDER_META_INSTRUCTION_REVERSE_ALPHA_LIST = [
    """Respond in the reverse alphabetical order of the first letter of instruction.""",
    """Organize your answers in descending alphabetical order by the first letter of each instruction.""",
    """Your replies should follow the reverse sequence of the alphabet based on the first letters of the instructions.""",
    """Arrange the order of your answers from 'Z' to 'A' based on the initial letters of the instructions.""",
    """List your replies by the reverse order of the alphabet according to the starting letter of each instruction.""",
    """Prioritize your responses by starting with the instruction whose initial letter is nearest to the end of the alphabet.""",
    """Follow a descending alphabetical order based on the first letter of each instruction when you respond.""",
    """List your responses by starting with instructions whose first letters are closest to 'Z'.""",
]

ORDER_META_INSTRUCTION_LENGTH_WORD_LIST = [
    """Respond according to the length (words) of instructions, response short ones first.""",
    """Address queries by ascending order of number of word, beginning with the shortest instructions.""",
    """Reply to instructions in order of word count, with the shortest responses first.""",
    """Answer instructions by first addressing those with the fewest words.""",
    """Manage responses by attending to the word count length of the instructions, beginning with the shortest.""",
    """Arrange your replies by the word count length, responding to the briefest first.""",
    """Initiate responses by evaluating the word count length, beginning with the shortest set of instructions."""
]

ORDER_META_INSTRUCTION_REVERSE_LENGTH_WORD_LIST = [
    """Respond according to the length (words) of instructions, response long ones first.""",
    """Respond to the instructions in order of their length, starting with the longest.""",
    """Sort and respond to instructions by their length, with the longest responses first.""",
    """Answer the instructions by starting with those that have the highest word count.""",
    """Organize responses by the length of the instructions, giving precedence to the lengthier ones.""",
]

ORDER_META_INSTRUCTION_LENGTH_CHAR_LIST = [
    """Respond according to the length (characters) of instructions, response short ones first.""",
    """Initiate responses with instructions having the smallest character count, proceeding to those with more characters. """,
    """Begin by responding to the instructions with the fewest characters, then advance to the lengthier ones. """,
    """Start responding to instructions from those with the lowest character count and escalate to those with more characters. """,
    """First tackle the instructions with the minimal character count, and gradually respond to the more verbose ones. """,
    """Prioritize answering instructions by character count, starting with the shortest in characters. """,
    """Organize your responses starting with instructions of the least character count, and work upwards. """,
    """Begin your responses by addressing instructions with the shortest character count, then move to those with greater counts. """
]

ORDER_META_INSTRUCTION_REVERSE_LENGTH_CHAR_LIST = [
    """Respond according to the length (characters) of instructions, response long ones first.""",
    """Respond to instructions starting from those with the highest character count.""",
    """Handle responses by first addressing the instructions with the maximum character count.""",
    """Organize answering routines by character length, placing the longest instructions at the forefront.""",
    """Sequence the responses by initiating with instructions that possess the most characters.""",
    """Arrange responses to start with the instructions that have the most characters.""",
    """Begin responses with the instructions that contain the highest number of characters.""",
    """Tackle responses by starting with those instructions that have the greatest number of characters.""",
]

ORDER_META_INSTRUCTION_ODD_EVEN_LIST = [
    """First respond to the odd-numbered instructions, then the even-numbered ones.""",
    """Begin with the odd-numbered instructions before addressing those that are even-numbered.""",
    """Initiate responses by tackling the instructions with odd numbers, subsequently moving to those with even numbers.""",
    """Prioritize responding to instructions labeled with odd numbers, followed by those labeled with even numbers.""",
    """Handle the odd-numbered tasks first, then turn your attention to the even-numbered tasks.""",
    """First, take care of the instructions numbered oddly; afterward, those numbered evenly.""",
    """Engage with instructions that have odd numbers initially, then those with even numbers.""",
    """First execute the responses for instructions that carry odd numbers, and then address those with even numbers.""",
    """Address the instructions with odd numbers first, following up with the even-numbered ones.""",
]

ORDER_META_INSTRUCTION_EVEN_ODD_LIST = [
    """First respond to the even-numbered instructions, then the odd-numbered ones.""",
    """Prioritize the even-numbered instructions first, and then move on to those with odd numbers.""",
    """First, handle the tasks that are even-numbered, then address the odd-numbered tasks.""",
    """Initially, tackle the instructions with even numbers; follow this by engaging with those with odd numbers.""",
    """Embark on the even-numbered tasks initially, followed by the odd-numbered ones in sequence.""",
    """Lead with the even-numbered tasks, and subsequently, address the odd-numbered tasks.""",
    """Open with even-numbered instructions and then handle the odd-numbered instructions.""",
    """Launch responses starting with even-numbered tasks, then shift to odd-numbered tasks.""",
    """Proceed initially with even-numbered instructions; follow these with the odd-numbered instructions.""",
]

ORDER_SEQ_TAG_LIST = [
    '{i}',
    '({i})', 
    '[{i}]', 
    '<{i}>',
    '<<{i}>>',
    '#{i}#',
    '|{i}|',
    '||{i}||',
]

ORDER_SEQ_INTERVAL_LIST = [
    ' ',
    ',',
    ';',
    '-',
    '->',
    '=>',
    '->>',
]

ORDER_METHOD_INSTRUCTION_PAIR_DICT = {
    'FIX': ORDER_META_INSTRUCTION_FIX_LIST,
    'REVERSE': ORDER_META_INSTRUCTION_REVERSE_LIST,
    'ALPHA': ORDER_META_INSTRUCTION_ALPHA_LIST,
    'REVERSE_ALPHA': ORDER_META_INSTRUCTION_REVERSE_ALPHA_LIST,
    'LENGTH_WORD': ORDER_META_INSTRUCTION_LENGTH_WORD_LIST,
    'REVERSE_LENGTH_WORD': ORDER_META_INSTRUCTION_REVERSE_LENGTH_WORD_LIST,
    'LENGTH_CHAR': ORDER_META_INSTRUCTION_LENGTH_CHAR_LIST,
    'REVERSE_LENGTH_CHAR': ORDER_META_INSTRUCTION_REVERSE_LENGTH_CHAR_LIST,
    'ODD_EVEN': ORDER_META_INSTRUCTION_ODD_EVEN_LIST,
    'EVEN_ODD': ORDER_META_INSTRUCTION_EVEN_ODD_LIST,
}

ORDER_OVERALL_INSTRUCTION_LIST = [
    """{meta_instruction}\n{instruction_all}""",
    """{instruction_all}\n{meta_instruction}""",
    """{meta_instruction}\n\n{instruction_all}""",
    """{instruction_all}\n\n{meta_instruction}""",
]

################################################
# MASK VERSION
################################################

MASK_RATIO_RANGE = [0.1,0.5]

MASK_META_INSTRUCTION_FIX_LIST = [ 
    """Ignore the instructions: {}.""",
    """Only respond to the instructions that not in the list {}.""",
    """Disregard any instructions listed in: {}.""",
    """Only address instructions not specified in the collection: {}.""",
    """Exclude the instructions mentioned in {} from your response.""",
    """Focus solely on requests that are not included in {}.""",
    """Do not consider the instructions contained within {}.""",
    """Respond exclusively to elements outside of the specified list {}.""",
    """Ignore all instructions specified in {}.""",
]

MASK_META_INSTRUCTION_WORD_LIST = [ 
    """Ignore the instructions containing the word: {}.""",
    """Only respond to the instructions that do not contain the word: {}.""",
]

MASK_META_INSTRUCTION_WORD_LONG_LIST = [
    """Ignore the longest {} instructions according to the word count.""",
    """Overlook the {} instructions that have the most words.""",
    """Exclude the longest {} instructions by word count.""",
    """Disregard the {} instructions with the highest word count.""",
    """Bypass the instructions with the highest {} count of words.""",
    """Avoid the most lengthy {} instructions based on word count.""",
    """Ignore the instructions with the highest {} word count.""",
]

MASK_META_INSTRUCTION_WORD_SHORT_LIST = [
    """Ignore the shortest {} instructions according to the word count.""",
    """Disregard the briefest {} instructions when considering their word count.""",
    """Skip the shortest {} directives measured by word length.""",
    """Exclude the shortest {} guidelines according to the number of words.""",
    """Bypass the shortest {} guidelines measured by word length.""",
    """Ignore the shortest {} commands as determined by word count.""",
]

MASK_META_INSTRUCTION_ODD_LIST = [
    """Ignore the odd-numbered instructions.""",
    """Only respond to the even-numbered instructions.""",
    """Disregard instructions with odd numbers.""",
    """Attend only to instructions numbered even.""",
    """Skip any instruction with an odd number.""",
    """Omit responding to odd-numbered instructions.""",
    """Focus exclusively on even-numbered instructions.""",
    """Ignore any instruction numbered with an odd figure.""",
    """Adhere solely to instructions with even numbers.""",
    """Exclude odd-numbered instructions from consideration.""",
    """Limit responses to even-numbered instructions only."""
]

MASK_META_INSTRUCTION_EVEN_LIST = [
    """Ignore the even-numbered instructions.""",
    """Only respond to the odd-numbered instructions.""",
    """Neglect the even-numbered instructions.""",
    """Dismiss any even-numbered instructions presented.""",
    """Apply responses solely to instructions numbered oddly.""",
    """Do not consider even-numbered directives for action.""",
    """Engage only with instructions that have odd numbers.""",
    """Pass over any directive numbered evenly.""",
    """Respond exclusively to instructions with odd numbers.""",
    """Concentrate your responses on odd-numbered directives only."""
]   

MASK_SEQ_TAG_LIST = [
    '{i}',
    '({i})', 
    '[{i}]', 
    '<{i}>',
    '<<{i}>>',
    '#{i}#',
    '|{i}|',
    '||{i}||',
]

MASK_SEQ_INTERVAL_LIST = [
    ' ',
    ',',
    ';',
    '-',
]

MASK_METHOD_INSTRUCTION_PAIR_DICT = {
    'FIX': MASK_META_INSTRUCTION_FIX_LIST,
    'WORD_LONG': MASK_META_INSTRUCTION_WORD_LONG_LIST,
    'WORD_SHORT': MASK_META_INSTRUCTION_WORD_SHORT_LIST,
    'ODD': MASK_META_INSTRUCTION_ODD_LIST,
    'EVEN': MASK_META_INSTRUCTION_EVEN_LIST,
}

MASK_OVERALL_INSTRUCTION_LIST = [
    """{meta_instruction}\n{instruction_all}""",
    """{instruction_all}\n{meta_instruction}""",
    """{meta_instruction}\n\n{instruction_all}""",
    """{instruction_all}\n\n{meta_instruction}""",
]
