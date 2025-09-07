from nicegui import ui,app
from Sections import hero, welcome


# Expose the assets folder to the nicegui server
app.add_static_files("/assets","assets")

# Load font awesome for socials
ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
                 
<link rel="stylesheet" href="/assets/reset.css"/>
''')


# animation
ui.add_head_html("""
<style>
@keyframes typing-loop {
  0% { width: 0; }
  40% { width: 100%; }
  90% { width: 100%; }
  100% { width: 0; }
}

.typewriter {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: typing-loop 7s steps(12, end) infinite;
}
</style>
""")


# google fonts
ui.add_head_html('''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lobster&family=Poppins:wght@100&display=swap" rel="stylesheet">
<style>
        .font-poppins{font-family:'Poppins', sans-serif;}
        .font-roboto {font-family; 'Roboto', sans-serif;}
        .font-lobster {font-family: 'Lobster', cursive;}
        .font {font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif}
</style>              
''')




hero.render()
welcome.render()

ui.run()