#!/usr/bin/env python
import sublime, sublime_plugin
import re

class TaskpaperPriorityCommand(sublime_plugin.TextCommand):
  def cycle_priority(self, line, up):
    up = True if up == "True" else False

    lowest_pri = 5

    pri_match = re.compile("@priority\\((\\d+)\\)")
    line_present = pri_match.search(line)

    if line_present:
      priority = int(pri_match.search(line).group(1))

      if up:
        if priority >= lowest_pri:
          new_priority = 1
        else:
          new_priority = priority + 1
      else:
        if priority == 1:
          new_priority = lowest_pri
        else:
          new_priority = priority - 1

      line = pri_match.sub("@priority({0})".format(new_priority), line)
    else:
      if up:
        line += " @priority(1)"
      else:
        line += " @priority({0})".format(lowest_pri)
    
    return(line)

  def run(self, edit, up):
    sels = self.view.sel()

    for sel in sels:
      lines = self.view.line(sel)
      updated_lines = self.cycle_priority(self.view.substr(lines), up)
      self.view.replace(edit, lines, updated_lines)



  # tasks = [task for task in sample_text.splitlines() if task != '']

  # for task in tasks:
    # print(cycle_priority(task))
#     def wrap_comment(self, line):
#       line_length = max(len(s) for s in line.split('\n'))
#       comment_line = '#' + '-' * (line_length + 1)
#       return(comment_line + '\n' + line + '\n' + comment_line)

#     def run(self, edit):
#       sels = self.view.sel()

#       for sel in sels:
#         lines = self.view.line(sel)
#         wrapped_code = self.wrap_comment(self.view.substr(lines))
#         self.view.replace(edit, lines, wrapped_code)

# sample_text = """
# - This is a todo @today
  # - This is another thing @priority(1)
# """


